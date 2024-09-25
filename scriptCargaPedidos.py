import os
import django
from datetime import datetime  # Mantén esta importación

# NO CALCULA EL PRECIO TOTAL DEL PEDIDO, SOLO CARGA PEDIDOS DE EJEMPLO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FruitAdmin.settings')
django.setup()

from pedidos.models import Pedido, PedidoProducto
from productos.models import Producto
from clientes.models import Cliente

def cargar_pedidos():
    productos = Producto.objects.all()  # Obtén todos los productos de la base de datos
    clientes = Cliente.objects.all()  # Obtén todos los clientes de la base de datos
    
    datos_pedidos = [
        {'cliente': clientes[0], 'productos': [{'producto': productos[0], 'cantidad': 4}], 'fecha_pedido': datetime(2024, 8, 1)},
        {'cliente': clientes[1], 'productos': [{'producto': productos[3], 'cantidad': 3}, {'producto': 'Producto 1', 'cantidad': 4}], 'fecha_pedido': datetime(2024, 8, 8)},
        {'cliente': clientes[1], 'productos': [{'producto': productos[2], 'cantidad': 4}, {'producto': 'Producto 4', 'cantidad': 5}], 'fecha_pedido': datetime(2024, 8, 17)},
        {'cliente': clientes[0], 'productos': [{'producto': productos[8], 'cantidad': 2}, {'producto': 'Producto 5', 'cantidad': 4}, {'producto': 'Producto 2', 'cantidad': 1}], 'fecha_pedido': datetime(2024, 7, 25)},
        {'cliente': clientes[1], 'productos': [{'producto': productos[7], 'cantidad': 1}, {'producto': 'Producto 6', 'cantidad': 3}], 'fecha_pedido': datetime(2024, 8, 1)},
        {'cliente': clientes[2], 'productos': [{'producto': productos[9], 'cantidad': 2}], 'fecha_pedido': datetime(2024, 8, 10)},
    ]

    for pedido_data in datos_pedidos:
        total_precio = 0  # Inicializa el precio total para cada pedido
        # Asociar los productos y calcular el precio total
        for producto_data in pedido_data['productos']:
            try:
                producto = Producto.objects.get(nombre=producto_data['producto'])  # Asegúrate de obtener el objeto Producto
                cantidad = producto_data['cantidad']
                total_precio += producto.costo * cantidad  # Asumiendo que el modelo Producto tiene un campo 'precio'
            except Producto.DoesNotExist:
                print(f"Producto '{producto_data['producto']}' no encontrado.")
                continue  # O maneja el error como prefieras

        # Crear el pedido con el precio total calculado
        pedido = Pedido.objects.create(
            cliente=pedido_data['cliente'],
            precio_total=total_precio,  # Asignar el precio total calculado
            fecha=pedido_data['fecha_pedido'],
        )

    # Asociar los productos al pedido
    for producto_data in pedido_data['productos']:
        try:
            producto = Producto.objects.get(nombre=producto_data['producto'])
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=producto_data['cantidad']
            )
        except Producto.DoesNotExist:
            print(f"Producto '{producto_data['producto']}' no encontrado al asociar al pedido.")
            continue
# Ejecuta la función para cargar los pedidos
cargar_pedidos()
