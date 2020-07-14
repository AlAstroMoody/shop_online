from .models import ProductInBasket


def get_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    total_quantity = products_in_basket.count()
    return locals()
