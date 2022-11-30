from django import forms
from django.contrib.auth.forms import UserCreationForm
from Usuarios.models import User

#birth = forms.DateField(label="fecha de nacimiento", widget=forms.DateInput)
class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2','tipo']
    widgets = {'tipo':forms.HiddenInput()}
    help_texts = {k: "" for k in fields}
  def __init__(self, *args, **kwargs):
    """If no initial data, provide some defaults."""
    #from django.forms.widgets import HiddenInput
    initial = kwargs.get('initial', {})
    initial['tipo'] = 'C'
    kwargs['initial'] = initial
    super(UserRegisterForm, self).__init__(*args, **kwargs)

class EmployeeRegisterForm(UserCreationForm):
  email = forms.EmailField()
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2','tipo']
    widgets = {'tipo':forms.HiddenInput()}
    help_texts = {k: "" for k in fields}
  def __init__(self, *args, **kwargs):
    """If no initial data, provide some defaults."""
    #from django.forms.widgets import HiddenInput
    initial = kwargs.get('initial', {})
    initial['tipo'] = 'E'
    kwargs['initial'] = initial
    super(EmployeeRegisterForm, self).__init__(*args, **kwargs)
