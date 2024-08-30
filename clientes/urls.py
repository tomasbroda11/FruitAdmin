from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_list, name='cliente_list'),
    path('alta-cliente/', views.clientes_create, name='cliente_create'),
    path('<int:pk>/', views.clientes_detail, name='cliente_detail'),
]
