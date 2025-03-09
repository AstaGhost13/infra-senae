from django import forms
from .models import Department, Floor

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['status', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
            'status': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')], attrs={'class': 'form-control'}),
        }
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['status', 'description', 'parent', 'id_floor']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripción',
            }),
            'parent': forms.Select(attrs={
                'class': 'form-control custom-select',
            }),
            'id_floor': forms.Select(attrs={
                'class': 'form-control custom-select',
            }),
        }