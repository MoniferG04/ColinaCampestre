from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import Lote, Servicio

class LoteCreateForm(forms.ModelForm):
    class Meta:
        model=Lote
        fields=('ancho','largo','matricula','precio','zona','estado','servicio')

class ServicioCreateForm(forms.ModelForm):
    class Meta:
        model=Servicio
        fields=('tipo','precio')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'correo',
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'password': 'password',
        }

class TerrenoForm(ModelForm):
    
    class Meta:
        model = Lote
        fields = ['matricula','ancho','largo','precio','zona']
        
