from django import forms
from .models import Custodian, Department, Floor, Position

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
            'status': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')], attrs={'class': 'form-control'}),
        }
        

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['status', 'description', 'department']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripción',
            }),
            'department': forms.Select(attrs={
                'class': 'form-control custom-select',
            }),
            'status': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')], attrs={'class': 'form-control'}),
        }


class CustodianForm(forms.ModelForm):
    class Meta:
        model = Custodian
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'reference', 'email', 'position']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el número de teléfono',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la dirección',
            }),
            'reference': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la referencia',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el correo electrónico',
            }),
            'position': forms.Select(attrs={
                'class': 'form-control custom-select',
            }),
            'status': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')], attrs={'class': 'form-control'}),
        }