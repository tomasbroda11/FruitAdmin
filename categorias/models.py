from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(null=False, max_length=35)

    def __str__(self):
        return self.nombre
    
    def contar_productos(self):
        return self.producto_set.count() 

