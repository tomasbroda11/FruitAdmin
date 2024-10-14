from django.db import models
from categorias.models import Categoria
from proveedores.models import Proveedor

class Producto(models.Model):
    UNIDAD = 'unidad'
    PESO = 'peso'
    
    TIPO_MEDIDA_CHOICES = [
        (UNIDAD, 'Unidad'),
        (PESO, 'Peso (kg)'),
    ]

    nombre = models.CharField(max_length=25, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    
    tipo_medida = models.CharField(
        max_length=10,
        choices=TIPO_MEDIDA_CHOICES,
        default=UNIDAD
    )

    def __str__(self):
        return self.nombre

    def calcular_precio_venta(self):
        return self.costo + (self.costo * self.porcentaje_ganancia / 100)