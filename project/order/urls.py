from django.urls import path, include

from .views import OrderView, Basket, basket_add

app_name = 'order'
urlpatterns = [
    path('', OrderView.as_view()),
    path('basket/', Basket.as_view(), name='basket'),
    path('basket_add/', basket_add, name='basket_add'),

]
