from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop.views import About, RegistrationView, Logout

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('order/', include('order.urls'), name='order'),
                  path('product/', include('product.urls')),
                  path('about/', About.as_view(), name='about'),
                  path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
                  path('registration/', RegistrationView.as_view(), name='registration'),
                  path('', include('shop.urls')),
                  path('logout/', Logout.as_view(), name='logout'),



              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
