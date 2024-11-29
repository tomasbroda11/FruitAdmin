from django.urls import path
from . import views

urlpatterns = [
    path('', views.mediospago_list, name='medios_pago_list'),
    path('crear/',views.mediospago_create, name='medios_pago_create'),
    path('editar/<int:pk>/', views.mediospago_update, name='medios_pago_update'),
    path('eliminar/<int:pk>/', views.mediospago_delete, name='medios_pago_delete'),
    path('detalles/<int:pk>/', views.mediospago_detail, name='medios_pago_details'),
]
