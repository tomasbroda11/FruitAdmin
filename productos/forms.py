from django import forms
from .models import Producto
from django.forms import inlineformset_factory
from categorias.models import Categoria

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Producto
        fields = ('nombre','categoria','costo', 'cantidad', 'porcentaje_ganancia')