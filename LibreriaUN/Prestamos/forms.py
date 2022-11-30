from django import forms
from .models import Prestamo
from Usuarios.models import Empleado,Cliente
from Libros.models import Libro
 
class PresForm(forms.ModelForm):
  Libros = Libro.objects.filter(estado__exact='D')
  libro = forms.ModelChoiceField(queryset=Libros)

  class Meta:
    model = Prestamo
    fields = ['estado', 'fecha_prestamo','fecha_devolucion', 'cliente', 'empleado', 'libro']
    widgets = {'empleado': forms.HiddenInput(), 'fecha_prestamo': forms.SelectDateWidget,
               'fecha_devolucion': forms.SelectDateWidget}

    help_texts = {k: "" for k in fields}

  def __init__(self, *args, **kwargs):
    """If no initial data, provide some defaults."""
    #from django.forms.widgets import HiddenInput
    initial = kwargs.get('initial', {})
    id_emp = kwargs.pop('id')
    initial['empleado'] = Empleado.objects.get(usuario=id_emp)
    kwargs['initial'] = initial
    super(PresForm, self).__init__(*args, **kwargs)
