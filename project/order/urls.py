from django.urls import path, include

from .views import OrderView, basket, basket_add

app_name = 'order'
urlpatterns = [
    path('', OrderView.as_view()),
    path('basket/', basket, name='basket'),
    path('basket_add/', basket_add, name='basket_add'),

]
