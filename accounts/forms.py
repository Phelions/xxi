from django import forms
from .models import Usuario

class Registro(forms.ModelForm):

    password1 = forms.CharField(label= 'Contraseña',widget=forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required' :'required',
        }
    ))
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id': 'password2',
            'required' :'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','rut','nombre','apellido','celular')
        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Correo',
                }
            ),
            'rut' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Ingrese su rut',
                }
            ),
            'nombre': forms.TextInput(
                attrs  = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su apellido',
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su celular',
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas nos coinciden!!')
        return password2
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


