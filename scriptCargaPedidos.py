import os
import django

# NO CALCULA EL PRECIO TOTAL DEL PEDIDO, SOLO CARGA PEDIDOS DE EJEMPLO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FruitAdmin.settings')
django.setup()

from pedidos.models import Pedido, PedidoProducto
from productos.models import Producto
from clientes.models import Cliente
from datetime import datetime

def cargar_pedidos():
    productos = Producto.objects.all()  # Obtén todos los productos de la base de datos
    clientes = Cliente.objects.all()  # Obtén todos los clientes de la base de datos
    
    datos_pedidos = [
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[0], 'cantidad': 2},
                {'producto': productos[1], 'cantidad': 1},
            ],
            'fecha_pedido': datetime(2024, 3, 24),
        },
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[7], 'cantidad': 11},
                {'producto': productos[5], 'cantidad': 2},
            ],
            'fecha_pedido': datetime(2024, 3, 8),
        },
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[3], 'cantidad': 23},
                {'producto': productos[7], 'cantidad': 12},
            ],
            'fecha_pedido': datetime(2024, 3, 4),
        },
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[0], 'cantidad': 2},
                {'producto': productos[3], 'cantidad': 18},
            ],
            'fecha_pedido': datetime(2024, 4, 2),
        },
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[10], 'cantidad': 20},
                {'producto': productos[8], 'cantidad': 19},
                {'producto': productos[5], 'cantidad': 9},
                {'producto': productos[6], 'cantidad': 6},
            ],
            'fecha_pedido': datetime(2024, 4, 9),
        },
        {
            'cliente': clientes[0],  # Referencia al primer cliente
            'productos': [
                {'producto': productos[0], 'cantidad': 2},
                {'producto': productos[6], 'cantidad': 12},
                {'producto': productos[4], 'cantidad': 11},
                {'producto': productos[3], 'cantidad': 5},
            ],
            'fecha_pedido': datetime(2024, 4, 21),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[2], 'cantidad': 13},
                {'producto': productos[0], 'cantidad': 45},
            ],
            'fecha_pedido': datetime(2024, 5, 4),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[5], 'cantidad': 13},
                {'producto': productos[4], 'cantidad': 14},
            ],
            'fecha_pedido': datetime(2024, 5, 22),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[2], 'cantidad': 9},
                {'producto': productos[4], 'cantidad': 6},
                {'producto': productos[5], 'cantidad': 14},
                {'producto': productos[7], 'cantidad': 7},
            ],
            'fecha_pedido': datetime(2024, 5, 14),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[2], 'cantidad': 3},
                {'producto': productos[0], 'cantidad': 4},
            ],
            'fecha_pedido': datetime(2024, 5, 24),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[7], 'cantidad': 13},
                {'producto': productos[4], 'cantidad': 22},
            ],
            'fecha_pedido': datetime(2024, 6, 1),
        },
        {
            'cliente': clientes[0],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[2], 'cantidad': 3},
                {'producto': productos[0], 'cantidad': 4},
                {'producto': productos[6], 'cantidad': 12},
                {'producto': productos[4], 'cantidad': 11},
            ],
            'fecha_pedido': datetime(2024, 6, 24),
        },
        {
            'cliente': clientes[1],  # Referencia al segundo cliente
            'productos': [
                {'producto': productos[2], 'cantidad': 3},
                {'producto': productos[1], 'cantidad': 4},
                {'producto': productos[6], 'cantidad': 5},
                {'producto': productos[8], 'cantidad': 14},
            ],
            'fecha_pedido': datetime(2024, 6, 13),
        }
    ]

    for pedido_data in datos_pedidos:
        # Crear el pedido
        pedido = Pedido.objects.create(
            cliente=pedido_data['cliente'],
            fecha=pedido_data['fecha_pedido'],
        )
        # Asociar los productos al pedido
        for producto_data in pedido_data['productos']:
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=producto_data['producto'],
                cantidad=producto_data['cantidad']
            )

    print(f"Se han cargado {len(datos_pedidos)} pedidos correctamente.")

# Ejecuta la función para cargar los pedidos
cargar_pedidos()
