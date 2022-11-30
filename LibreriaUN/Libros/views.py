from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Libro,Genero
from .forms import BookForm

# Create your views here.

def Libros(request):
  if(request.GET["prd"]):   
    search = request.GET["prd"]
    libros = Libro.objects.filter(nombre__icontains=search)
    return render(request, "Libros/libros.html", {"libros": libros})
  else:
    libros = Libro.objects.all()
    return render(request, "Libros/libros.html", {"libros": libros})

@permission_required('Usuarios.Permiso_Empleado', login_url="../login")  # type: ignore
def CrearLibro(request):
  if (request.method == 'POST'):
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      nombre=form.cleaned_data['nombre']
      messages.success(request, f'libro {nombre} creado')
      return redirect('/')
  else:
    form = BookForm()
  return render(request, "Libros/crear.html", {"form": form})

def MostrarLibro(request,libro_id):
  libro = Libro.objects.get(pk=libro_id)
  return render(request, "Libros/libro.html",{"libro":libro})


@permission_required('Usuarios.Permiso_Empleado', login_url="../login")  # type: ignore
def ActualizarLibro(request,libro_id):
  libro = Libro.objects.get(pk=libro_id)
  if (request.method == 'POST'):
    form = BookForm(request.POST, instance=libro)
    if form.is_valid():
      form.save()
      nombre = form.cleaned_data['nombre']
      messages.success(request, f'libro {nombre} actualizado')
      return redirect('/libros/?prd=')
  else:
    form = BookForm(instance=libro)
  return render(request, "Libros/actualizar.html", {"form": form})
