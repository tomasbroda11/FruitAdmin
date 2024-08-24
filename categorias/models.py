from django.db import models

class Categoria(models.Model):
    nombre = models.TextField(null=False)

    def __str__(self):
        return self.nombre
