from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ProductsView, ProductDetail

app_name = 'product'

urlpatterns = [
                  path('', ProductsView.as_view(), name='product'),
                  path('<str:id>/', ProductDetail.as_view(),
                       name='product_details_url'),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
