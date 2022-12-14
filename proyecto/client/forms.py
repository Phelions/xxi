from django import forms
from django.forms import ModelForm, TextInput, HiddenInput
from manager.models import AccountUsuario
from manager.models import Reserva, EstadoMesa, Mesa, AccountUsuario
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



class ReservaForm(ModelForm):
    id_reserva = forms.IntegerField(required=False, widget=forms.HiddenInput())
    id_usuario = forms.IntegerField(required=False, label="Usuario", widget=forms.HiddenInput())
    id_mesa = forms.ModelChoiceField(queryset=Mesa.objects.all().order_by('id_mesa'), required=True, label="Mesa")
    fecha = forms.DateField(required=True, label="Fecha", widget=NumberInput(attrs={'type':'date', 'min':'2022-01-12', 'max':'2020-12-31 23:59:59', 'step':'1'}))
    hora = forms.TimeField(required=True, label="Hora",widget=NumberInput(attrs={'type':'time' , 'min':'00:00:00', 'max':'23:59:59', 'step':'1'}))
    class Meta:
        model = Reserva
        fields = ['id_reserva','id_usuario','id_mesa', 'fecha','hora']


class res_login_mesas(ModelForm):
    rut = forms.CharField(required=True, label="Rut", widget=TextInput(attrs={'placeholder':'Rut', 'min':'100000000', 'max':'999999999', 'step':'1' ,'title':'9 numeros - rut sin puntos y guion, remplace "K" por 0'}))
    class Meta:
        model = AccountUsuario
        fields = ['rut']
