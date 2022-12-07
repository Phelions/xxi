from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Mesa

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'
