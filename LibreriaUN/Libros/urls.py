from django.urls import path
from . import views

urlpatterns = [
    path('', views.Libros, name='Libros'),
    path('crear/', views.CrearLibro, name='Crear'),
]