from django.shortcuts import render, redirect
from manager.models import Usuario, Empleado
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        checklogin = Usuario.objects.filter(email=email, password=password).values()
        if checklogin:
            request.session['estadoSesion'] = True
            request.session['idUser'] = checklogin[0]['id']
            request.session['TipoUser'] = checklogin[2][1]
            request.session['TipoUser'] = checklogin[2][2]
            request.session['TipoUser'] = checklogin[2][3]
            request.session['TipoUser'] = checklogin[2][4]
            request.session['TipoUser'] = checklogin[2][5]
            request.session['TipoUser'] = checklogin[2][6]
            request.session['TipoUser'] = checklogin[2][7]
            request.session['TipoUser'] = checklogin[2][8]
            if checklogin[2] == 1:
                return redirect(request, 'dashboard/client/reservar.html')
            elif checklogin[2] == 2:
                return redirect(request, 'dashboard/manager/empleados_admin.html')
            # elif checklogin[2] == 3:
            #     return redirect(request, 'dashboard/#')
            # elif checklogin[2] == 4:
            #     return redirect(request, 'dashboard/#')
            # elif checklogin[2] == 5:
            #     return redirect(request, 'dashboard/#')
            # elif checklogin[2] == 6:
            #     return redirect(request, 'dashboard/#')
            # elif checklogin[2] == 7:
            #     return redirect(request, 'dashboard/#')
            # elif checklogin[2] == 8:
            #     return redirect(request, 'dashboard/#')
        else:
            checklogin = {'r2' : 'Error de Usuario y/o Contraseña!!'}
            return render(request, 'accounts/login.html', checklogin)
    else:
        datos = {'r2' : 'No se puede procesar la solicitud'}
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')