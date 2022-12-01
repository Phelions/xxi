from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class LoginForm(forms.Form):
    email = forms.CharField (
        widget= forms.EmailInput(
            attrs = {
                "placeholder": "Correo",
                "class": "form-control"
            }
        ),
        error_messages={
            'required': 'Los campos son obligatorios'
            }
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
    rut = forms.IntegerField(
        widget= forms.NumberInput(
            attrs = {
                "class": "form-control",
                "placeholder": "111111110"
            }
        )
    , label=''
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Nombre"
            }
        )
    , label=''
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Apellido"
            }
        )
    , label=''
    )
    celular = forms.IntegerField(
        widget= forms.NumberInput(
            attrs = {
                "class": "form-control",
                "placeholder": "celular"
            }
        )
    , label=''
    )

    email = forms.CharField(
        widget= forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Correo"
            }
        )
    , label=''
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Contraseña"
            }
        )
    , label=''
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Repita su contraseña"
            }
        )
    , label=''
    )
    class Meta:
        model = User
        fields = ('rut','first_name','last_name','celular','email','password1','password2')