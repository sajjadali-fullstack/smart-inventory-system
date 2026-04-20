from django import forms
from .models import Products

# Yahan ModelSerializer ki jagah ModelForm likhein
class ProductForm(forms.ModelForm): 
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'product_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'mfg': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }