from django import forms
from .models import Categoria
from django.forms import inlineformset_factory

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nombre',)