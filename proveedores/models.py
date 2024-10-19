from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    cuit = models.CharField(max_length=11)
    
    def __str__(self) -> str:
        return self.nombre
