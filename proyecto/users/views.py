from django.shortcuts import render
# from .models import Usuario
# Create your views here.


def login(request):

#    if request.method == 'POST':
#        email = request.POST['email']
#        password = request.POST['password']
#        checklogin = Usuario.objects.filter(email=email, password=password).values()       
#        if checklogin:
#            print(checklogin[0])
#        else:
#            checklogin = {'r2' : 'Error de Usuario y/o Contraseña!!'}
#            return render(request, 'accounts/login.html', checklogin)
#    else:
#        datos = {'r2' : 'No se puede procesar la solicitud'}
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')