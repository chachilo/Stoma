# tienda/models.py
from django.db import models

class Computadora(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    destacada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

