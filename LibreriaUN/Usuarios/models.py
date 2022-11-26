from django.db import models
#from Usuarios.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  image = models.ImageField(null=True)
  TIPOS = {
      ('C', 'Cliente'),
      ('E', 'Empleado'),
  }
  tipo = models.CharField(null=True ,max_length=1, choices=TIPOS)
  class Meta:
    permissions = (
      ('Permiso_Empleado','tiene acceso a CRUD de datos'),
      ('Permiso_Cliente','tiene acceso a vistas basicas')
    )

  
class Empleado(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  fecha_contrato = models.DateTimeField(default=timezone.now)
  permissions={

  }
  class Meta:
    verbose_name = "empleado"
    verbose_name_plural = "empleados"

  def __str__(self):
    return f'empleado {self.usuario.username}'

class Cliente(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  fecha_registro = models.DateTimeField(default=timezone.now)
  
  class Meta:
    verbose_name = "cliente"
    verbose_name_plural = "clientes"

  def __str__(self):
    return f'cliente {self.usuario.username}'


