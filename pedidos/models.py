from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from datetime import datetime

class Pedido(models.Model):
    
    ESTADO_OPCIONES = [
        ('en_espera', 'En espera'),
        ('procesado', 'Procesado'),
        ('entregado', 'Entregado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    fecha = models.DateTimeField(default=datetime.now)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='en_espera')

    def __str__(self):
        if self.cliente:
            return f"Pedido {self.id} - {self.cliente.nombre}"
        else:
            return f"Pedido {self.id} - Cliente desconocido"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.pedido.id}"
