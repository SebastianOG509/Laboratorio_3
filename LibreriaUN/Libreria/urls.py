from django.urls import path 
from Libreria import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contacto/', views.contacto, name='Contacto'),
]
