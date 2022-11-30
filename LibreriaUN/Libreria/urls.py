from django.urls import path 
from Libreria import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('contacto/', views.contacto, name='Contacto'),
    path('nosotros/', views.sobre_nosotros, name='Nosotros'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)