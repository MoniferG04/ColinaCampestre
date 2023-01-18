from django import forms

from .models import Lote

class LoteCreateForm(forms.ModelForm):
    class Meta:
        model=Lote
        fields=('ancho','largo','matricula','precio','zona','estado','servicio')
