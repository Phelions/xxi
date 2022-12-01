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
    rut = forms.IntegerField(
        widget= forms.NumberInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    nombre = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    apellido = forms.CharField(
        widget= forms.TextInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    celular = forms.IntegerField(
        widget= forms.NumberInput(
            attrs = {
                "class": "form-control",
            }
        )
    )

    email = forms.CharField(
        widget= forms.EmailInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                "class": "form-control",
            }
        )
    )
    class Meta:
        model = User
        fields = ('rut','nombre','apellido','celular','email','password1','password2')