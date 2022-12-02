from django.shortcuts import render, redirect
from .forms import  LoginForm, SignupForm
from django.contrib.auth import authenticate, login as django_login
from axes.decorators import axes_dispatch
from django.http import HttpResponse
# Create your views here.

@axes_dispatch
def login(request):
    form = LoginForm(request.POST)
    msg=None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request,email=email, password=password)
            if user is not None and user.is_client:
                django_login(request, user)
                return redirect('reservar')
            elif user is not None and user.is_admin:
                django_login(request, user)
                return redirect('administrar_clientes')
            elif user is not None and user.is_finanzas:
                login(request, user)
                return redirect('reservar')
            elif user is not None and user.is_bodega:
                login(request, user)
                return redirect('reservar')
            elif user is not None and user.is_cocina:
                login(request, user)
                return redirect('reservar')
            elif user is not None and user.is_barman:
                login(request, user)
                return redirect('reservar')
            elif user is not None and user.is_garzon:
                login(request, user)
                return redirect('reservar')
            else:
                msg = 'Correos o contraseña incorrectos'
        else:
            msg = 'Error al crear usuario'
    return render(request, 'accounts/login.html', {'form':form, 'msg':msg})

def lockout(request, credentials, *args, **kwargs):
    return HttpResponse("Bloqueado debido a demasiadas fallas de inicio de sesión| Contacte al Administrador | <a href='/'>Volver</a>")

def signup(request):
    msg=None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Usuario creado correctamente'
            return redirect ("login")
        else:
            msg = 'Error al crear usuario'
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form':form, 'msg':msg})