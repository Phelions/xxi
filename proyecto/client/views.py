from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from .forms import ReservaForm
from manager.models import Reserva, EstadoMesa, Mesa, AccountUsuario
# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def res_mesa(request):
    return render(request, 'dashboard/mesas/index.html')




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
    
# def add_reserva(id_usuario, id_mesa, fecha_hora):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     salida = cursor.var(cx_Oracle.NUMBER)
#     cursor.callproc('SP_CREAR_RESERVA', [id_usuario, id_mesa, fecha_hora, salida])
#     return salida.getvalue()

def listar_mesas(request):
    data = {
        'mesas': listado_estados_mesas,
    }
    return render(request, 'dashboard/client/crear.html', data)

@login_required
def crear_reserva(request):
    if request.user.is_client:
        msg = None
        if request.method == 'POST':
            form = ReservaForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.id_usuario = request.user.id_usuario
                obj.save()
                msg = 'Reserva ingresada correctamente'
                return redirect('reservas')
            else:
                msg = 'Error al ingresar su reserva'
        else:
            form = ReservaForm(request.POST)
        return render(request, 'dashboard/client/reservar.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def reservas(request):
    if request.user.is_client:
        data = {
            'reservas': listado_reservas()
        }
        return render(request, 'dashboard/client/index.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/client/reservas.html')

def listado_reservas():
    reserva = Reserva.objects.select_related("id_usuario").select_related("id_mesa").all()
    lista = []
    for fila in reserva:
        lista.append(fila)
    return lista

def listado_estados_mesas():
    estados = Mesa.objects.select_related("id_empleado").select_related("id_est_me").all()
    lista = []
    for fila in estados:
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

