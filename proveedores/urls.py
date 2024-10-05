from django.urls import path
from . import views

urlpatterns = [
    path('', views.proveedores_list, name='proveedores_list'),
    path('alta-proveedor/', views.proveedores_create, name='proveedor_create'),
    path('<int:pk>/', views.proveedores_detail, name='proveedor_detail'),
    path('<int:pk>/delete/', views.proveedores_delete, name='proveedor_delete'),
    path('<int:pk>/update/', views.proveedores_update, name='proveedor_update'),
]