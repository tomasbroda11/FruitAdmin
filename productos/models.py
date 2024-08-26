from django.db import models
from categorias.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=25 , null=False)
    cantidad = models.IntegerField(null=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
