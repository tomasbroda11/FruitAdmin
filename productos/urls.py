from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_list, name='producto_list'),
    path('alta-producto/', views.productos_create, name='producto_create'),
    path('<int:pk>/', views.productos_detail, name='producto_detail'),
]
