from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
# Create your views here.

def index(request):
    return render(request, 'index.html')


'''----Dashboard - cliente---'''


@login_required
def menu(request):
    if request.user.is_client:
        data = {
            'mesas': listado_estados_mesas(),
        }
        return render(request, 'dashboard/client/menu.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/menu.html')
    

def add_reserva(id_usuario, id_mesa, fecha_hora):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(NUMBER)
    cursor.callproc('SP_CREAR_RESERVA', [id_usuario, id_mesa, fecha_hora, salida])
    return salida.getvalue()

def listar_mesas(request):
    data = {
        'mesas': listado_estados_mesas,
    }
    return render(request, 'dashboard/client/crear.html', data)

def listado_estados_mesas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_MESAS', [out_cur])

    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
        }
        lista.append(data)
    return lista

@login_required
def crear_reserva(request):
    if request.user.is_client:
        data = {
            'mesas': listado_estados_mesas(),
        }
        msg=None
        if request.method == 'POST':
            id_usuario = request.POST.get('id_usuario')
            id_mesa = request.POST.get('id_mesa')
            fecha_hora = request.POST.get('fecha_hora')
            salida = add_reserva(id_usuario, id_mesa, fecha_hora)
            if salida == 1:
                data['mensaje'] = 'reservado correctamente'
                data['mesas'] = listado_estados_mesas()
            else:
                data['mensaje'] = 'no se ha podido reservar'
        return render(request, 'dashboard/client/crear.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def reservas(request):
    if request.user.is_client:
        data = {
            'listarreservas': listado_reservas()
        }
        return render(request, 'dashboard/client/index.html',data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/reservas.html')

def listado_reservas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_RESERVAS', [out_cur])

    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
        }
        lista.append(data)
    return lista


@login_required
def perfil(request):
    if request.user.is_client:
        return render(request, 'dashboard/client/perfil.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/perfil.html')

'''----Dashboard - cliente - FIN---'''

