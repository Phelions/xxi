from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Usuario, Empleado
from manager.models import Mesa , EstadoMesa, Menu, TipoMenu, AccountEmpleado, AccountUsuario, Receta
from crispy_forms.helper import FormHelper

TURNO = [
    ('Full-Time', 'Full-Time'),
]

ROL = [
    ('Mesa', 'Mesa'),
]


class UsuarioMesaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all().filter(first_name='mesa'), required=True)
    rol = forms.ChoiceField(choices=ROL, widget=forms.HiddenInput())
    turno = forms.ChoiceField(choices=TURNO, initial='Full-Time', widget=forms.HiddenInput())
    hora_entrada = forms.TimeField(required=True, label="Hora Entrada")
    hora_salida = forms.TimeField(required=True, label="Hora Salida")
    class Meta:
        model = Empleado
        fields = ['usuario','rol','turno','hora_entrada','hora_salida']


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
    ('2', 'Ocupada'),
    ('3', 'Reservada'),
    ('4', 'Deshabilitada'),
]


class MesasForm(forms.ModelForm):
    id_mesa = forms.IntegerField(required=True, label="N?? Mesa", widget= forms.NumberInput(attrs={'min':'1', 'max':'1000'}))
    id_est_me = forms.ModelChoiceField(label="Estado de la mesa", required=True, queryset=EstadoMesa.objects.all())
    capacidad = forms.IntegerField(label="Capacidad de personas",required=True)
    id_empleado = forms.ModelChoiceField(queryset=AccountEmpleado.objects.all(), required=True, label="Empleado encargado")
    class Meta:
        model = Mesa
        fields = ['id_mesa','id_est_me','capacidad','id_empleado']
        
        
class MenuForm(forms.ModelForm):
    id_menu = forms.IntegerField(required=True, label="N?? Menu", widget= forms.NumberInput(attrs={'min':'1', 'max':'500'}))
    id_tipo_m = forms.ModelChoiceField(queryset=TipoMenu.objects.all(),label="Tipo de menu", required=True)
    nombre_m = forms.CharField(required=True, label="Nombre")
    precio = forms.IntegerField(required=True, label="Precio")
    class Meta:
        model = Menu
        fields = ['id_menu','id_tipo_m','nombre_m','detalle','porcion','tiempo','precio']

class TipoMenuForm(forms.ModelForm):
    id_tipo_m = forms.IntegerField(required=True, label="N?? Menu",  widget= forms.NumberInput(attrs={'min':'1', 'max':'500'}))
    descripcion = forms.CharField(required=True, label="PLato, Bebida, Postre, etc")
    class Meta:
        model = TipoMenu
        fields = ['id_tipo_m','descripcion']


class RecetaForm(forms.ModelForm):
    id_receta = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    id_empleado = forms.ModelChoiceField(queryset=AccountEmpleado.objects.all(), required=False, label="Empleado encargado",widget=forms.HiddenInput())
    id_menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=True, label="Menu")
    nombre_receta = forms.CharField(required=True, label="Nombre")
    ingredientes = forms.CharField(required=True, label="Ingredientes")
    preparacion = forms.CharField(required=True, label="Preparacion")
    class Meta:
        model = Receta
        fields = ['id_receta', 'id_empleado','id_menu','nombre_receta','ingredientes','preparacion']
