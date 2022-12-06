from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from manager.models import AccountUser
from .models import User
class LoginForm(forms.Form):
    email = forms.CharField (
        widget= forms.EmailInput(
            attrs = {
                "placeholder": "Correo",
                "class": "form-control"
            }
        )
    , label='')
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        )
    , label='')

class SignupForm(UserCreationForm):
    helper = FormHelper()
    is_client = forms.BooleanField( widget=forms.HiddenInput() ,initial=True)
    rut = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'9 numeros - rut sin puntos y guion, remplace "K" por 0'}))
    celular = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'Solo se aceptan numeros, Total = 9'}))
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    class Meta:
        model = User
        fields = ('rut','first_name','last_name','celular','email','password1','password2','is_client')
        

class SignupEmployeeForm(UserCreationForm):
    helper = FormHelper()
    rut = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'9 numeros - rut sin puntos y guion, remplace "K" por 0'}))
    celular = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'Solo se aceptan numeros, Total = 9'}))
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    
    class Meta:
        model = User
        fields = ['rut','first_name','last_name','celular','email','password1','password2','is_admin','is_finanza','is_bodega','is_cocina', 'is_barman','is_garzon']

class EmpleadoForm(UserCreationForm):
    helper = FormHelper()
    rut = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'9 numeros - rut sin puntos y guion, remplace "K" por 0'}))
    celular = forms.CharField(required=True,max_length=9, min_length=9, widget= forms.TextInput(attrs={'pattern':'[0-9]{9}','title':'Solo se aceptan numeros, Total = 9'}))
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    
    class Meta:
        model = User
        fields = ['rut','first_name','last_name','celular','email','password1','password2','is_admin','is_finanza','is_bodega','is_cocina', 'is_barman','is_garzon']
   
        
        
