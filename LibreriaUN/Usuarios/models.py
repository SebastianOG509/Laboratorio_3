from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
#from django.utils.translation import gettext_lazy as _

# Create your models here.


"""class User(AbstractUser):
  class Types(models.TextChoices):
    Cliente = "Cliente"
    Empleado = "Empleado"
  type = models.CharField(_("Type"), max_length= 20, choices=Types.choices, default=Types.Cliente)


class Empleado(User):
  class Meta:
    proxy = True

class Cliente(User):
  class Meta:
    proxy = True
"""

class Usuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField()

  class Meta:
    verbose_name = "usuario"
    verbose_name_plural = "usuarios"

  def __str__(self):
    return self.user.username
  
