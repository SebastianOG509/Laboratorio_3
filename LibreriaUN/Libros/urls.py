from django.urls import path
from . import views

urlpatterns = [
    path('', views.Libros, name='Libros'),
    path('crear/', views.CrearLibro, name='Crear'),
    path('producto/<int:libro_id>/', views.MostrarLibro,name='Producto'),
    path('producto/<int:libro_id>/actualizar', views.ActualizarLibro, name='Actualizar'),
]
