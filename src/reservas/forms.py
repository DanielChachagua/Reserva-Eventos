from django import forms
from .models import ReservaServicio
from clientes.models import Cliente
from coordinadores.models import Coordinador
from empleados.models import Empleado
from servicios.models import Servicio

class FormReserva(forms.Form):
    fecha_reserva=forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}))
    cliente=forms.ModelChoiceField(queryset=Cliente.objects.filter(activo=True))
    responsable=forms.ModelChoiceField(queryset=Coordinador.objects.filter(activo=True))
    empleado=forms.ModelChoiceField(queryset=Empleado.objects.filter(activo=True))
    servicio=forms.ModelChoiceField(queryset=Servicio.objects.filter(activo=True))
    precio=forms.DecimalField(decimal_places=2, max_digits=10)

class EditarFormReserva(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['fecha_reserva','cliente','responsable','empleado','servicio','precio']
        widgets = {
            'fecha_reserva':forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
        }