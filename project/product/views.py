from django.shortcuts import render
from django.views.generic import View, ListView

from product.models import Product


class ProductView(ListView):
    queryset = Product.objects.all()
