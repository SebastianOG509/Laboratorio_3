from django import forms
from .models import Libro


class CreateBookForm(forms.ModelForm):
  class Meta:
    model = Libro
    fields = ['ISBN', 'estado', 'nombre', 'genero','autor','año','descripcion','imagen']
