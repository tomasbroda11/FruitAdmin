from django import forms
from .models import Producto
from django.forms import inlineformset_factory
from categorias.models import Categoria
from proveedores.models import Proveedor
from django.core.exceptions import ValidationError


class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Producto
        fields = ('nombre', 'categoria', 'costo','precio' ,'cantidad', 'porcentaje_ganancia', 'tipo_medida', 'proveedor')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'porcentaje_ganancia': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'tipo_medida': forms.RadioSelect(choices=Producto.TIPO_MEDIDA_CHOICES),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'precio':forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['porcentaje_ganancia'].required = False

    def clean(self):
        cleaned_data = super().clean()
        
        forma_carga = cleaned_data.get('formaCarga')
        precio = cleaned_data.get('precio')
        porcentaje_ganancia = cleaned_data.get('porcentaje_ganancia')

        print(f"forma_carga: {forma_carga}, precio: {precio}, porcentaje_ganancia: {porcentaje_ganancia}")

        # Validar si seleccionaron la opción 'precio' y no ingresaron precio
        if forma_carga == 'precio' and not precio:
            self.add_error('precio', 'Debe ingresar un precio si seleccionó la opción Costo + Precio.')

        # Validar si seleccionaron la opción 'porcentaje_ganancia' y no ingresaron porcentaje
        elif forma_carga == 'porcentaje_ganancia' and not porcentaje_ganancia:
            self.add_error('porcentaje_ganancia', 'Debe ingresar un porcentaje de ganancia si seleccionó la opción Costo + % Ganancia.')

        return cleaned_data    


class ProductoUpdateForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    stock_actual = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    precio_actual = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    class Meta:
        model = Producto
        fields = ('producto', 'precio', 'cantidad')
        widgets = {
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }


class CargarExcelForm(forms.Form):
    archivo = forms.FileField(label='Seleccione el archivo', widget=forms.FileInput(attrs={'class': 'form-control'}))
    