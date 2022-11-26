from django.db.models.signals import post_save
from .models import Empleado,User
from django.dispatch import receiver


"""@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
  if created:
    if kwargs['email'] != "a":
      Empleado.objects.create(user=instance)"""
