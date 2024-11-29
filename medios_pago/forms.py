from django import forms
from .models import MedioPago
from django.forms import inlineformset_factory

class MediospagoForm(forms.ModelForm):
    
    class Meta:
        model = MedioPago
        fields = ('nombre',)

class MediospagoUpdateForm(forms.ModelForm):
    cateogria = forms.ModelChoiceField( queryset=MedioPago.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = MedioPago
        fields = ('nombre',)
        widget = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
