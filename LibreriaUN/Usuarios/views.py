from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import User,Empleado,Cliente
from .forms import UserRegisterForm, EmployeeRegisterForm
from django.dispatch import Signal
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group

def Usuarios(request):
  usuario = request.user
  if(request.user.is_authenticated):
    return render(request,'Usuarios/usuario.html',{"usuario":usuario})
  else:
    #messages.info(request,"Primero registrate")
    return redirect('/usuarios/login/')


def Register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      usuario = form.save()
      Cliente.objects.create(usuario=usuario)
      grupo=Group.objects.get(name='Cliente')
      usuario.groups.add(grupo)
      
      username = form.cleaned_data['username']
      messages.success(request, f'usuario {username} creado')
      login(request,usuario)
      return redirect('/')
  else:
    form = UserRegisterForm()

  context = {'form': form}
  return render(request, "Usuarios/registro.html", context)


@permission_required('Usuarios.add_user',login_url="../login")  # type: ignore
def RegistroEmpleado(request):
  if request.method == 'POST':
    
    form = EmployeeRegisterForm(request.POST)
    if form.is_valid():
      usuario = form.save()
      Empleado.objects.create(usuario=usuario)
      grupo = Group.objects.get(name='Empleados')
      usuario.groups.add(grupo)
      username = form.cleaned_data['username']
      messages.success(request, f'empleado {username} creado')
      return redirect('/')
  else:
    form = EmployeeRegisterForm()

  context = {'form': form}
  return render(request, "Usuarios/registroEmpleado.html", context)
  
