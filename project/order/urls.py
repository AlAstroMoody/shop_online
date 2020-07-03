from django.urls import path, include

from .views import OrderView

urlpatterns = [
    path('', OrderView.as_view(), name='home')
]
