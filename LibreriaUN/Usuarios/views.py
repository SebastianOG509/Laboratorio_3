from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import Usuario
from .forms import UserRegisterForm


def Usuarios(request):
  usuario = request.user
  if(request.user.is_authenticated):
    return render(request,'Usuarios/usuario.html',{"usuario":usuario})
  else:
    messages.info(request,"Primero registrate")
    return redirect('register')

def Register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      usuario = form.save()
      username = form.cleaned_data['username']
      messages.success(request, f'usuario {username} creado')
      login(request,usuario)
      return redirect('../../')
  else:
    form = UserRegisterForm()

  context = {'form': form}
  return render(request, "Usuarios/registro.html", context)

  
