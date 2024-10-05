from django import forms
from .models import Producto
from django.forms import inlineformset_factory
from categorias.models import Categoria

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Producto
        fields = ('nombre','categoria','costo', 'cantidad', 'porcentaje_ganancia', 'tipo_medida')
        widgets = {
            'cantidad': forms.NumberInput(attrs={'step': 'any'}),
            'tipo_medida': forms.RadioSelect(choices=Producto.TIPO_MEDIDA_CHOICES),
        }

class ProductoUpdateForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    stock_actual = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    precio_actual = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    class Meta:
        model = Producto
        fields = ('producto', 'costo', 'cantidad')
        widgets = {
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }


class CargarExcelForm(forms.Form):
    archivo = forms.FileField(label='Seleccione el archivo', widget=forms.FileInput(attrs={'class': 'form-control'}))
    