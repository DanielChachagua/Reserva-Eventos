from typing import Any
from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm

class FormCliente(UserChangeForm):
    password=None
    class Meta:
        model=Cliente
        fields=[
            'nombre',
            'apellido',
            'email',
            'dni'
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Email',
            'dni':'DNI'
        }
    
class EditarFormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","email","dni"]    
    