from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'Libreria/home.html')

def contacto(request):

    return render(request, "Libreria/contacto.html")
