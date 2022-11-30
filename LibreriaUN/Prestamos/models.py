from django.db import models
from Usuarios.models import Cliente, Empleado
from Libros.models import Libro

# Create your models here.
class Prestamo(models.Model):
    estado = models.BooleanField()
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
