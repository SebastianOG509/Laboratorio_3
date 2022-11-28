from django.urls import path 
from Libreria import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contacto/', views.contacto, name='Contacto'),
    path('nosotros/', views.sobre_nosotros, name='Nosotros'),
]
