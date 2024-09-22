
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),
    path('productos/', include('productos.urls')),
    path('clientes/', include('clientes.urls')),
    path('reportes/', include('reportes.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
