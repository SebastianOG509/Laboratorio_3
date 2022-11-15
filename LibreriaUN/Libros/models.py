from django.db import models
import datetime

# Create your models here.


class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "genero"
        verbose_name_plural = "generos"

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    ESTADOS = {
        ('D', 'Disponible'),
        ('N', 'No Disponible'),
        ('P', 'En prestamo'),
    }
    AÑOS = []
    for r in range(0, (datetime.datetime.now().year+1)):
        AÑOS.append((r, r))
    ISBN = models.IntegerField()
    estado = models.CharField(max_length=1, choices=ESTADOS)
    nombre = models.CharField(max_length=80)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    año = models.IntegerField(choices=AÑOS)

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"

    def __str__(self):
        return self.nombre
    
