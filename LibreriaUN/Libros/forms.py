from django import forms
from .models import Libro,Genero


class BookForm(forms.ModelForm):
  class Meta:
    model = Libro
    fields = ['ISBN', 'estado', 'nombre', 'genero','autor','año','descripcion','imagen']

class GenreForm(forms.ModelForm):
  class Meta:
    model = Genero
    fields = ['nombre']