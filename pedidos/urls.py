from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('<int:pk>/delete/', views.pedido_delete, name='pedido_delete'),
    path('nuevo/', views.pedido_create, name='pedido_create'),
    path('get_productos/', views.get_productos, name='get_productos'),
    path('eliminar_seleccionados/', views.eliminar_pedidos_seleccionados, name='eliminar_pedidos_seleccionados'),
]
