from django.shortcuts import render,HttpResponse

# Create your views here.


def Books(request):

  return HttpResponse("Books")  ##render(request, "WebApp/book.html")
