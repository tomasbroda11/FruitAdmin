import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FruitAdmin.settings')
django.setup()

from pedidos.models import Pedido, PedidoProducto
from productos.models import Producto
from clientes.models import Cliente

def cargar_pedidos():
    # Obtiene todos los productos y clientes existentes
    productos = list(Producto.objects.all())
    clientes = list(Cliente.objects.all())

    if not productos or not clientes:
        print("No hay productos o clientes en la base de datos para cargar pedidos.")
        return

    # Datos de prueba para los pedidos
    datos_pedidos = [
        {
            'cliente': clientes[0],
            'productos': [
                {'producto': productos[3], 'cantidad': 3},
                {'producto': productos[2], 'cantidad': 3},
                {'producto': productos[6], 'cantidad': 3},
                {'producto': productos[6], 'cantidad': 3},
                {'producto': productos[1], 'cantidad': 3},
                {'producto': productos[5], 'cantidad': 5}
            ],
            'fecha_pedido':"2024-08-12 08:43:35",
            'estado': 'procesado'
        },
        {
            'cliente': clientes[1],
            'productos': [
                {'producto': productos[8], 'cantidad': 1},
                {'producto': productos[1], 'cantidad': 2}
            ],
            'fecha_pedido': "2024-11-11 09:41:05",
            'estado': 'en espera'
        },
        {
            'cliente': clientes[2],
            'productos': [
                {'producto': productos[4], 'cantidad': 1},
                {'producto': productos[3], 'cantidad': 3},
                {'producto': productos[7], 'cantidad': 4},
                {'producto': productos[1], 'cantidad': 5}
            ],
            'fecha_pedido': "2024-11-15 10:23:50",
            'estado': 'entregado'
        }
    ]

    # Itera sobre los datos y crea pedidos y sus productos
    for pedido_data in datos_pedidos:
        total_precio = 0
        productos_data = pedido_data.pop('productos')  # Separa los productos para procesarlos por separado

        # Calcula el precio total del pedido
        for producto_data in productos_data:
            producto = producto_data['producto']
            cantidad = producto_data['cantidad']
            total_precio += producto.precio * cantidad

        # Crea el pedido
        pedido = Pedido.objects.create(
            cliente=pedido_data['cliente'],
            precio_total=total_precio,
            fecha=pedido_data['fecha_pedido'],
            estado=pedido_data['estado']
        )

        # Asocia los productos al pedido
        for producto_data in productos_data:
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=producto_data['producto'],
                cantidad=producto_data['cantidad']
            )

        print(f"Pedido creado: {pedido} con {len(productos_data)} productos.")

# Ejecuta la función para cargar los pedidos
if __name__ == "__main__":
    cargar_pedidos()
