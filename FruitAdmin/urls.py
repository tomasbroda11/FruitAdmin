
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import home 


urlpatterns = [
     path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pedidos/', include('pedidos.urls')),
    path('productos/', include('productos.urls')),
    path('clientes/', include('clientes.urls')),
    path('reportes/', include('reportes.urls')),
    path('proveedores/',include('proveedores.urls')),
    path('categorias/',include('categorias.urls')),
    path('mediospago/',include('medios_pago.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
