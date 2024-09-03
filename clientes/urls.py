from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_list, name='cliente_list'),
    path('alta-cliente/', views.clientes_create, name='cliente_create'),
    path('<int:pk>/', views.clientes_detail, name='cliente_detail'),
    path('<int:pk>/delete/', views.clientes_delete, name='cliente_delete'),
    path('paises/', views.get_paises, name='get_paises'),
    path('provincia/<str:pais_iso2>/', views.get_provincias, name='get_provincias'),
    path('ciudades/<str:pais_iso2>/<str:provincia_iso2>/', views.get_ciudades, name='get_ciudades'),
]
