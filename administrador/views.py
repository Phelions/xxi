from django.shortcuts import render
from django.db import connection
import cx_Oracle
# Create your views here.


def dashboard(request):

    data = {
        'menu': list_menu()
    }

    if request.method == 'POST':
        id_menu = request.POST.get('id_menu')
        nombre_m = request.POST.get('nombre')
        porcion = request.POST.get('porcion')
        detalle = request.POST.get('detalle')
        precio = request.POST.get('precio')
        imagen = request.FILES['imagen'].read()
        salida = add_menu(id_menu, nombre_m, porcion, detalle, precio)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['menu'] = list_menu()
        else:
            data['mensaje'] = 'no se ha podido agregar'

    return render(request, 'administrador/home/dashboard.html', data)

def list_menu():
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

def add_menu(id_menu, nombre_m, porcion, detalle, precio):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_MENU', [id_menu, nombre_m, porcion, detalle, precio, salida])
    return salida.getvalue()

def add_empleado(rut ,id_tipo, nombre, p_apellido, celular, correo, contrasena,id_empleado, id_rol, id_turno, hora_entrada, hora_salida):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_empleado', [rut ,id_tipo, nombre, p_apellido, celular, correo, contrasena,id_empleado, id_rol, id_turno, hora_entrada, hora_salida,salida])
    return salida.getvalue()
