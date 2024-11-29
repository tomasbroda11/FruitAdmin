from django.db import models

class MedioPago(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False, blank=False)
    

    def __str__(self):
        return self.nombre
