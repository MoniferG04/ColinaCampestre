from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Lote

class LoteCreateForm(forms.ModelForm):
    class Meta:
        model=Lote
        fields=('ancho','largo','matricula','precio','zona','estado','servicio')

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
