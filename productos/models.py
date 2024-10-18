from django.db import models
from categorias.models import Categoria
from proveedores.models import Proveedor
from decimal import Decimal
from django.core.exceptions import ValidationError

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
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    
    tipo_medida = models.CharField(
        max_length=10,
        choices=TIPO_MEDIDA_CHOICES,
        default=UNIDAD
    )


    def calcular_precio(self):
        
        if self.porcentaje_ganancia:
            return self.costo * (1 + self.porcentaje_ganancia / 100)
        return self.precio
    
    def save(self, *args, **kwargs):
        
        if not self.precio and self.porcentaje_ganancia:
            self.precio = self.calcular_precio()
        elif not self.porcentaje_ganancia and self.precio:
            self.porcentaje_ganancia = ((self.precio / self.costo) - 1) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre