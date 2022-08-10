from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ecommerce.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecom.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

