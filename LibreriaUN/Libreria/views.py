from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'Libreria/home.html')

def libros(request):

    return HttpResponse("Libros")

def usuarios(request):

    return HttpResponse("Usuarios")

def contacto(request):

    return render(request, "Libreria/contacto.html")
