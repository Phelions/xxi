from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'client/home/index.html')


'''----Dashboard - cliente---'''

@login_required
def menu(request):
    if request.user.is_client:
        return render(request, 'dashboard/client/menu.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/menu.html')

@login_required
def reservar(request):
    if request.user.is_client:
        return render(request, 'dashboard/client/reservar.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/reservar.html')

@login_required
def reservas(request):
    if request.user.is_client:
        return render(request, 'dashboard/client/reservas.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/reservas.html')

@login_required
def perfil(request):
    if request.user.is_client:
        return render(request, 'dashboard/client/perfil.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/perfil.html')

'''----Dashboard - cliente - FIN---'''