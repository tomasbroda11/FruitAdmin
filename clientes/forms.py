from django import forms
from .models import Cliente
from django.forms import inlineformset_factory

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nombre','cuit','email','telefono', 'direccion')