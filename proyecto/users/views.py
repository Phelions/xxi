from django.shortcuts import render
from .models import Usuario
# Create your views here.


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        checklogin = Usuario.objects.filter(email=email, password=password).values()

    else:
        datos = {'r2' : 'No se puede procesar la solicitud'}
    return render(request, 'accounts/login.html',datos)

def logout(request):
    return render(request, 'accounts/logout.html')