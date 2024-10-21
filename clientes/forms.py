from django import forms
from .models import Cliente
from django.forms import inlineformset_factory

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nombre','cuit','email','telefono', 'direccion')

class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cuit','email', 'telefono', 'direccion','ciudad','provincia']  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
        }