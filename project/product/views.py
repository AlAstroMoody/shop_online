from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from product.models import Product


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        # Product.load_detail()
        return render(request, './products.html', locals())


class ProductDetails(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id__iexact=id)
        return render(request, 'product-details.html',
                      locals())
