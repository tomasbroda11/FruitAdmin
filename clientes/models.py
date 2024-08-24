from django.db import models

class Cliente(models.Model):
    nombre = models.TextField(null=False)
    email = models.TextField(blank=True, null= True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
