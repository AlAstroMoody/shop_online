from django.urls import path, include

from .views import Basket, basket_add, OrderView

app_name = 'order'
urlpatterns = [

    path('basket/', Basket.as_view(), name='basket'),
    path('basket_add/', basket_add, name='basket_add'),
    path('order/', OrderView.as_view(), name='order_view'),

]
