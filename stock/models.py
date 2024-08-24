from django.db import models
from productos.models import Producto

class MovimientoStock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movimiento {self.id} - {self.producto.nombre}"
