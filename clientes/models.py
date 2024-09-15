from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(null=False, max_length=35)
    cuit = models.CharField(max_length=35)
    email = models.EmailField(blank=True, null= True, max_length=35)
    direccion = models.CharField(blank=True, null=True, max_length=35 )
    telefono = models.CharField(blank=True, null=True, max_length=35)

    def __str__(self):
        return self.nombre


