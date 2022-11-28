from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'Libreria/home.html')

def contacto(request):

    return render(request, "Libreria/contact.html")

def sobre_nosotros(request):

    return render(request, "Libreria/nosotros.html")
