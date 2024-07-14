from django import forms
from .models import ContactForm, Comuna  # Asegúrate de importar los modelos necesarios

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['nombre', 'rut', 'dv', 'telefono', 'direccion', 'comuna', 'profesion', 'sexo', 'ocupacion', 'puesto_empresa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'dv': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }
