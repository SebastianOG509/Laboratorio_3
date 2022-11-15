from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField()

  class Meta:
    verbose_name = "usuario"
    verbose_name_plural = "usuarios"

  def __str__(self):
    return self.user.username
  
