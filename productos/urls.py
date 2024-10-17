from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_list, name='producto_list'),
    path('alta-producto/', views.productos_create, name='producto_create'),
    path('<int:pk>/', views.productos_detail, name='producto_detail'),
    path('<int:pk>/delete/', views.productos_delete, name='producto_delete'),
    path('update/', views.productos_update, name='producto_update'),
    path('api/producto/<int:pk>/', views.productos_api_detail, name='producto_api_detail'),
    path('upload-excel/', views.productos_upload_excel, name='producto_upload_excel'),
    path('update/masivo', views.update_masivo, name='update_masivo'),
]
