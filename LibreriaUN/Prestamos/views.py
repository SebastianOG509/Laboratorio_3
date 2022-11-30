from django.shortcuts import render
from .models import Prestamo, Libro, Cliente, Empleado


# Create your views here.
def Prestar(request):

    return render(request, "Prestamos/prestamo.html")

def Hacer_prestamo(request, cliente_id, empleado_id, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    cliente = Cliente.objects.get(pk=libro_id)
    Prestamo = Empleado.objects.get(pk=libro_id)
    
    return render(request, "Prestamos/prestamo.html")

