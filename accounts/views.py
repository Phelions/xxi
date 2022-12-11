from django.shortcuts import render
from .forms import Registro
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuario


class Register(CreateView):
    model = Usuario
    form_class = Registro
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
