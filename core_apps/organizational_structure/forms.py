from django import forms
from .models import Floor

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['status', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }