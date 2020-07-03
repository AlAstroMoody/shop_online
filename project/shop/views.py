from django.shortcuts import render
from django.views.generic import View

from product.models import ProductImage


class Home(View):
    def get(self, request):
        product_images = ProductImage.objects.filter(is_active=True, is_main_image=True)[:3]
        return render(request, './home.html', locals())
