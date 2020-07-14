from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.models import User

from order.models import Order, ProductInBasket


class OrderView(ListView):
    queryset = Order.objects.all()


@login_required
def basket(request):
    return render(request, 'basket.html', locals())


def basket_add(request):
    return_dict = dict()
    data = request.POST
    session_key = request.session.session_key
    product_id = data.get('product_id')
    quantity = data.get('quantityNum')
    is_delete = data.get('is_delete')
    if is_delete == 'true':
        ProductInBasket.objects.filter(product_id=product_id).update(is_active=False)

    else:
        order = Order.objects.create(customer_name=request.user, status_id=1)
        order_id = order.id
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, order_id=order_id)
        if not created:
            new_product.quantity += int(quantity)
        else:
            new_product.quantity = int(quantity)
        new_product.save(force_update=True)

    total_quantity = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()

    return_dict['total_quantity'] = total_quantity
    return_dict["products"] = list()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["quantityNum"] = item.quantity
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)
