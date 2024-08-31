from django.db import models



class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}, {self.pais.nombre}'

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}, {self.provincia.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(null=False, max_length=35)
    cuit = models.IntegerField(null=False, default='-')
    email = models.EmailField(blank=True, null= True, max_length=35)
    direccion = models.CharField(blank=True, null=True, max_length=35 )
    telefono = models.CharField(blank=True, null=True, max_length=35)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


