from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from product.models import Product


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        # Product.load_detail()
        return render(request, './products.html', locals())


class ProductDetails(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, id):
        product = get_object_or_404(Product, id__iexact=id)
        return render(request, 'product-details.html',
                      locals())


