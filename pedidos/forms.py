from django import forms
from .models import Pedido, PedidoProducto
from clientes.models import Cliente
from productos.models import Producto
from django.forms import inlineformset_factory

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoSelectWidget(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value and not isinstance(value, (int, str)):
            value = value.value
        if value:
            try:
                producto = Producto.objects.get(pk=value)
                option['attrs']['data-precio'] = str(producto.costo)
            except Producto.DoesNotExist:
                pass
        return option

class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': ProductoSelectWidget(attrs={'class': 'form-control producto-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control cantidad-input'}),
        }

class PedidoEstadoUpdate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']
        labels = {
            'estado': 'Actualizar Estado del Pedido',
        }
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }




PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1, can_delete=True)

