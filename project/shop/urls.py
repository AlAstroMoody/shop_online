from django.urls import path

from .views import Home, RegistrationView


urlpatterns = [
    path('', Home.as_view(), name='home'),
]

