from django.urls import path
from . import views

urlpatterns = [
    path('', views.categorias_list, name='categoria_list'),
    path('alta-categoria/', views.categorias_create, name='categoria_create'),
    path('<int:pk>/', views.categorias_detail, name='categoria_detail'),
    path('<int:pk>/delete/', views.categorias_delete, name='categoria_delete'),
    #path('<int:pk>/update/', views.categorias_update, name='categoria_update'),
   
]
