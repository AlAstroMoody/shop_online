from django.urls import path

from .views import Home, RegistrationView

app_name = 'home'
urlpatterns = [
    path('', Home.as_view(), name='home'),
]

