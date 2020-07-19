from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView

from product.models import Product


class ProductsView(ListView):
    queryset = Product.objects.all().order_by('-id')


class ProductDetail(DetailView):
    queryset = Product.objects.all()
    pk_url_kwarg = 'id'

