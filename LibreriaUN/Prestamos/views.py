from django.shortcuts import render,redirect
from django.contrib.auth.decorators import permission_required
from .models import Prestamo
from Usuarios.models import Cliente
from Libros.models import Libro
from .forms import PresForm

# Create your views here.

@permission_required('Usuarios.Permiso_Empleado', login_url="../login")  # type: ignore
def RealizarPrestamo(request):
  if not request.user.is_superuser:
    if request.method == 'POST':
      form = PresForm(request.POST,id=request.user.id)
      if form.is_valid():
        prestamo = form.save()
        libro = Libro.objects.get(pk=prestamo.libro.pk)
        libro.estado = 'N'
        libro.save(update_fields=['estado'])
        return redirect('/')
    else:
      form = PresForm(id=request.user.id)
    return render(request, "Prestamos/prestamo.html", {"form":form})
  return redirect('/')
#def ():


#@permission_required('Usuarios.Permiso_Cliente', login_url="../login")  # type: ignore
def MisPrestamos(request):
  if(request.user.is_authenticated):
    try:
      cliente = Cliente.objects.get(usuario=request.user.id)
    except:
      cliente = None
    if(cliente == None):
      prestamos =Prestamo.objects.all()
    else:
      prestamos = Prestamo.objects.filter(cliente=cliente.pk)
    return render(request, "Prestamos/misprestamos.html", {"prestamos":prestamos})
  else:
    return redirect("/usuarios/login/")
