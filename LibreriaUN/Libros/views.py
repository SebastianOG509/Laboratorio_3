from django.shortcuts import render

from .models import Libro,Genero
# Create your views here.

def Libros(request):
  if(request.GET["prd"]):   
    search = request.GET["prd"]
    libros = Libro.objects.filter(nombre__icontains=search)
    return render(request, "Libros/libros.html", {"libros": libros})
  else:
    libros = Libro.objects.all()
    return render(request, "Libros/libros.html", {"libros": libros})
