from django.urls import path
from . import views

urlpatterns = [
    path('', views.RealizarPrestamo, name='Prestamo'),
    path('misprestamos', views.MisPrestamos, name='MisPrestamos'),
]