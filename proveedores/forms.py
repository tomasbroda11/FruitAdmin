from django import forms
from .models import Proveedor
from django.forms import inlineformset_factory

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ('nombre','direccion','telefono','email', 'cuit')

class ProveedorUpdateForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'cuit','email', 'telefono', 'direccion']  # Agrega todos los campos que deseas actualizar.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
