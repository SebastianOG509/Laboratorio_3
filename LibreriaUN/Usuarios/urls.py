from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.Usuarios, name='Usuarios'),
    path('register/',views.Register,name="register"),
    path('login/',LoginView.as_view(template_name='Usuarios/login.html') ,name="login"),
    path('logout/', LogoutView.as_view(template_name='Usuarios/logout.html'), name="logout"),
]
