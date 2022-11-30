from django.shortcuts import render, HttpResponse
from Usuarios.models import User,Cliente,Empleado
from Libros.models import Libro
# Create your views here.

def home(request):

    return render(request, 'Libreria/home.html')

def contacto(request):

    return render(request, "Libreria/contact.html")

def sobre_nosotros(request):

    return render(request, "Libreria/nosotros.html")

def estadisticas(request):
    usuarios = User.objects.count()
    empleados = Empleado.objects.count()
    clientes = Cliente.objects.count()
    porc_empleados = round(empleados/usuarios*100,2)
    porc_clientes = round(clientes/usuarios*100,2)
    ##libros
    libros = Libro.objects.all().order_by("-likes")

    context={"libros":libros,"usuarios":usuarios,"empleados":empleados,"clientes":clientes,"porc_empleados":porc_empleados,"porc_clientes":porc_clientes}
    return render(request, "Libreria/estadisticas.html", context)
