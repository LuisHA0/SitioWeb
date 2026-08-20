from django.db import models


class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    producto = models.CharField(max_length=100, blank=True, default='')
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre
