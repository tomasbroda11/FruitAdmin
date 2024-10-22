from django import forms
from .models import Categoria
from django.forms import inlineformset_factory

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nombre',)

class CategoriaUpdateForm(forms.ModelForm):
    cateogria = forms.ModelChoiceField( queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Categoria
        fields = ('nombre',)
        widget = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
