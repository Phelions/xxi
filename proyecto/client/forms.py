from django import forms
from django.forms import ModelForm, TextInput, HiddenInput
from manager.models import AccountUsuario
from manager.models import Reserva, EstadoMesa, Mesa, AccountUsuario
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



class ReservaForm(ModelForm):
    id_usuario = forms.IntegerField(required=False, label="Usuario")
    id_mesa = forms.ModelChoiceField(queryset=Mesa.objects.all().order_by('id_mesa'), required=True, label="Mesa")
    fecha = forms.DateField(required=True, label="Fecha", widget=NumberInput(attrs={'type':'date', 'min':'2022-01-12', 'max':'2020-12-31 23:59:59', 'step':'1'}))
    hora = forms.TimeField(required=True, label="Hora",widget=NumberInput(attrs={'type':'time' , 'min':'00:00:00', 'max':'23:59:59', 'step':'1'}))
    class Meta:
        model = Reserva
        fields = ['id_usuario','id_mesa', 'fecha','hora']
