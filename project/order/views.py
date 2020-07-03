from django.shortcuts import render
from django.views.generic import View, ListView

from order.models import Order


class OrderView(ListView):
    queryset = Order.objects.all()