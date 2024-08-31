from django import forms
from .models import Cliente
from django.forms import inlineformset_factory

class ClienteForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Cliente
        fields = ('nombre','cuit','email','telefono', 'direccion','pais', 'provincia', 'ciudad')