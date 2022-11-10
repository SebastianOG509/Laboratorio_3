from django.urls import path

from . import views

urlpatterns = [
    path('',views.Books,name="Books"),
]
##to implemen more views
