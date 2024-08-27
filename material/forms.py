from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'type': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'thickness': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'step': '0.01'}),
            'width': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'step': '0.01'}),
            'height': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'step': '0.01'}),
            'color': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer_code': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'step': '0.01'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
        }
