from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Libro,Genero
from .forms import CreateBookForm

# Create your views here.

def Libros(request):
  if(request.GET["prd"]):   
    search = request.GET["prd"]
    libros = Libro.objects.filter(nombre__icontains=search)
    return render(request, "Libros/libros.html", {"libros": libros})
  else:
    libros = Libro.objects.all()
    return render(request, "Libros/libros.html", {"libros": libros})

def CrearLibro(request):
  if (request.method == 'POST'):
    form = CreateBookForm(request.POST)
    if form.is_valid():
      form.save()
      nombre=form.cleaned_data['nombre']
      messages.success(request, f'libro {nombre} creado')
      return redirect('/')
  else:
    form = CreateBookForm()
  return render(request, "Libros/crear.html", {"form": form})

def MostrarLibro(request,libro_id):
  libro = Libro.objects.get(pk=libro_id)
  return render(request, "Libros/libro.html",{"libro":libro})
