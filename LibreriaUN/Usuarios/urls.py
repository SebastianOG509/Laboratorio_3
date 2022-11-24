from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.Register, name='Registro'),
    path('login/',LoginView.as_view(template_name='Usuarios/login.html') ,name="Usuarios"),
    path('logout/', LogoutView.as_view(template_name='Usuarios/logout.html'), name="logout"),
    path('perfil/', views.Usuarios, name="perfil"),
]
