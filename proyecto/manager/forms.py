from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Usuario, Empleado
from manager.models import Mesa , EstadoMesa, Menu, TipoMenu, AccountEmpleado
from crispy_forms.helper import FormHelper

    


class SignupEmployeeForm(UserCreationForm):
    helper = FormHelper()
    id_usuario = forms.IntegerField(required=False, widget=forms.HiddenInput())
    username = forms.CharField(required=False, widget=forms.HiddenInput())
    is_employee = forms.BooleanField(initial=True,widget=forms.HiddenInput())
    rut = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'9 numeros - rut sin puntos y guion, remplace "K" por 0'}))
    celular = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'Solo se aceptan numeros, Total = 9'}))
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
   
    class Meta:
        model = Usuario
        fields = ['id_usuario','rut','first_name','last_name','celular','email','password1','password2']
    def save(self, *args, **kwargs):
        ...
        self.is_employee = True
        ...
        super(SignupEmployeeForm, self).save(*args, **kwargs)
        
TURNO = [
    ('Part-Time', 'Part-Time'),
    ('Full-Time', 'Full-Time'),
]

ROL = [
    ('Admin', 'Admin'),
    ('Mesa', 'Mesa'),
    ('Finanza', 'Finanza'),
    ('Bodega', 'Bodega'),
    ('Cocina', 'Cocina'),
    ('Barman', 'Barman'),
    ('Garzon', 'Garzon'),
]
    
class EmployeeForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True)
    rol = forms.ChoiceField(choices=ROL)
    turno = forms.ChoiceField(choices=TURNO)
    hora_entrada = forms.TimeField(required=True, label="Hora Entrada")
    hora_salida = forms.TimeField(required=True, label="Hora Salida")
    class Meta:
        model = Empleado
        fields = ['usuario','rol','turno','hora_entrada','hora_salida']

class TurForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True,widget=forms.HiddenInput())
    rol = forms.ChoiceField(choices=ROL)
    turno = forms.ChoiceField(choices=TURNO)
    hora_entrada = forms.TimeField(required=True, label="Hora Entrada")
    hora_salida = forms.TimeField(required=True, label="Hora Salida")
    class Meta:
        model = Empleado
        fields = ['usuario','rol','turno','hora_entrada','hora_salida']
        
ESTADO_MESA = [
    ('1', 'Disponible'),
    ('2', 'Reservada'),
    ('3', 'Ocupada'),
    ('4', 'Deshabilitada'),
]


class MesasForm(forms.ModelForm):

    id_est_me = forms.ChoiceField(choices=ESTADO_MESA,label="Estado de la mesa", required=True)
    capacidad = forms.IntegerField(label="Capacidad de personas",required=True)
    id_empleado = forms.ModelChoiceField(queryset=AccountEmpleado.objects.all(), required=True, label="Empleado encargado")
    class Meta:
        model = Mesa
        fields = ['id_est_me','capacidad','id_empleado']
        
        
class MenuForm(forms.ModelForm):
    id_menu = forms.IntegerField(required=True,  widget=forms.HiddenInput())
    id_tipo_menu = forms.ModelChoiceField(queryset=Menu.objects.all(),label="Tipo de menu", required=True)
    nombre_m = forms.CharField(required=True, label="Nombre")
    descripcion = forms.CharField(required=True, label="Descripcion")
    precio = forms.IntegerField(required=True, label="Precio")
    class Meta:
        model = Menu
        fields = ['id_menu','id_tipo_menu','nombre_m','detalle','porcion','tiempo','precio']

class TipoMenuForm(forms.ModelForm):
    id_tipo_m = forms.IntegerField(required=True)
    descripcion = forms.CharField(required=True, label="PLato, Bebida, Postre, etc")
    class Meta:
        model = TipoMenu
        fields = ['id_tipo_m','descripcion']

