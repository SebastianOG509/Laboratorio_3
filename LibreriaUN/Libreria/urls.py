from django.urls import path 
from Libreria import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('libros/', views.libros, name='Libros'),
    path('usuarios/', views.usuarios, name='Usuarios'),
    path('contacto/', views.contacto, name='Contacto'),
]
