import cx_Oracle
from django.shortcuts import render, redirect
from django.db import connection
from administrador.models import Menu, Mesa
from client.Carrito import Carrito
import base64
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'client/home/index.html')



# - END auth sesion  - #
@login_required(login_url='/index/')
def listarreservas(request):
    data = {
        'listarreservas': listado_reservas()
    }
    return render(request, 'client/reservation/listarreservas.html', data)

@login_required(login_url='/index/')
def reservar(request):
    data = {
        'estados': listado_estados_mesas(),
    }
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        id_mesa = request.POST.get('id_mesa')
        fecha_hora = request.POST.get('fecha_hora')
        salida = add_reserva(id_usuario, id_mesa, fecha_hora)
        if salida == 1:
            data['mensaje'] = 'reservado correctamente'
            data['estados'] = listado_estados_mesas()
        else:
            data['mensaje'] = 'no se ha podido reservar'

    return render(request, 'client/reservation/home.html', data)

def mesa(request):
    data = {
        'mesas': listado_mesas(),
    }
    return render(request, 'mesa/mesas.html', data)


def menu(request):
    data = {
        'menu': listado_menu(),
        'estados': listado_estados_mesas(),
    }
    return render(request, 'client/order/menu.html', data)

def boleta(request):
    data = {}
    return render(request, 'client/order/boleta.html')


def carrito(request):
    data = { 
        'menu': listado_menu(),
        'mesas': listado_estados_mesas(),
    }
    return render(request, 'client/order/carrito.html', data)

#### - Especial Carrito - ####

def agregar_menu_carrito(request, id_menu):
    carrito = Carrito(request)
    menu = Menu.objects.get(id_menu=id_menu)
    carrito.agregar(menu)
    return redirect(to="carrito")

def eliminar_menu_carrito(request, id_menu):
    carrito = Carrito(request)
    menu = Menu.objects.get(id_menu=id_menu)
    carrito.eliminar(menu)
    return redirect(to="carrito")

def restar_menu_carrito(request, id_menu):
    carrito = Carrito(request)
    menu = Menu.objects.get(id_menu=id_menu)
    carrito.restar(menu)
    return redirect(to="carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect(to="carrito")



##### - AGREGAR  - #####

def add_reserva(id_usuario, id_mesa, fecha_hora):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_CREAR_RESERVA', [id_usuario, id_mesa, fecha_hora, salida])
    return salida.getvalue()

def add_pedido(id_menu, id_mesa, cantidad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PEDIDO', [id_menu, id_mesa, cantidad, salida])
    return salida.getvalue()


##### - ELIMINAR  - #####

def eliminar_reserva(request, id_reserva):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RESERVA', [id_reserva, salida])
    return redirect(to="listarreservas")

def eliminar_pedido(request, id_pedido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_PEDIDO', [id_pedido, salida])
    return redirect(to="listarpedidos")


##### - END ELIMINAR  - #####

##### - LISTADOS  - #####

def listado_pedidos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_PEDIDOS', [out_cur])

    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
        }
        lista.append(data)
    return lista

def listado_menu():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_MENU', [out_cur])
    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
        }
        lista.append(data)
    return lista

def listado_mesas():
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

def listado_estados_mesas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc('SP_LISTAR_ESTADOS_MESAS', [out_cur])

    lista = []
    for fila in out_cur:
        data = {
            'data': fila,
        }
        lista.append(data)
    return lista

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

## -- MODIFICAR -- ##

def update_mesa(request,id_mesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_ESTADO_MESA', [id_mesa, salida])
    return redirect(to="mesa")

def up_mesa(request,id_mesa):
    data = {
        'listadomesas': listado_mesas(),
    }
    if request.method == 'POST':
        mesa_id = id_mesa
        salida = update_mesa(mesa_id)
        if salida == 1:
            data['mensaje'] = 'mesa pedida correctamente'
            data['listadomesas'] = listado_mesas()
        else:
            data['mensaje'] = 'no se ha podido pedir la mesa'

    return render(request, 'client/mesa/mesas.html', data)