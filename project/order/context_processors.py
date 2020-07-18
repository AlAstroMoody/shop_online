from django.contrib.auth.models import User

from .models import ProductInBasket


def get_basket_info(request):
    if not request.user.is_authenticated:
        is_anonymous = True
    else:
        is_anonymous = False
        user = User.objects.get(username=request.user)
        products_in_basket = ProductInBasket.objects.filter(order__user=user.id, is_active=True)
        total_quantity = products_in_basket.count()
        sum_quantity = 0
        for i in products_in_basket:
            sum_quantity += i.quantity
    return locals()
