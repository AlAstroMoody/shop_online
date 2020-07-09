from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django.contrib.auth import logout

from product.models import ProductImage


class Home(View):
    def get(self, request):
        product_images = ProductImage.objects.filter(is_active=True, is_main_image=True)[:3]
        return render(request, 'home.html', locals())


class About(View):
    def get(self, request):
        return render(request, 'about.html', locals())


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'registration/logout.html')


class RegistrationView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


@login_required
def basket(request):
    return render(request, 'basket.html', locals())

