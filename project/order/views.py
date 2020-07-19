from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from order.models import Order, ProductInBasket, ProductInOrder


class OrderView(ListView):
    pk_url_kwarg = 'id'
    template_name = 'order.html'

    def get_queryset(self):
        return Order.objects.all().filter(user=self.request.user)


class Basket(LoginRequiredMixin, ListView):
    queryset = ProductInBasket.objects.all()
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'basket.html'


def basket_add(request):
    return_dict = dict()
    data = request.POST
    product_id = data.get('product_id')
    quantity = data.get('quantityNum')
    is_delete = data.get('is_delete')
    return_dict['is_anonymous'] = False
    if not request.user.is_authenticated:
        return_dict['is_anonymous'] = True
    else:
        user = User.objects.get(username=request.user)
        if is_delete == 'true':
            ProductInBasket.objects.filter(product_id=product_id).update(is_active=False)
        else:
            order, created = Order.objects.get_or_create(user=user, is_active=True, status_id=1)
            new_product, created = ProductInBasket.objects.get_or_create(product_id=product_id,
                                                                         is_active=True, order_id=order.id,
                                                                         order__user=user.id)
            if not created:
                new_product.quantity += int(quantity)
            else:
                new_product.quantity = int(quantity)
            new_product.save(force_update=True)
        products_in_basket = ProductInBasket.objects.filter(order__user=user.id, is_active=True)
        total_quantity = products_in_basket.count()
        sum_quantity = 0
        for i in products_in_basket:
            sum_quantity += i.quantity

        return_dict['total_quantity'] = total_quantity
        return_dict['sum_quantity'] = sum_quantity
        return_dict["products"] = list()
        for item in products_in_basket:
            product_dict = dict()
            product_dict["id"] = item.id
            product_dict["name"] = item.product.name
            product_dict["price_per_item"] = item.price_per_item
            product_dict["quantityNum"] = item.quantity
            return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)
