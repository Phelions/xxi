from django.shortcuts import render, redirect
from account.forms import SignupEmployeeForm
from django.contrib.auth.decorators import login_required
from django.db import connection
# Create your views here.



'''----Dashboard - admin---'''
@login_required
def perfil_admin(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/perfil_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/perfil_admin.html')

@login_required
def listar_cliente(request):
    if request.user.is_admin:
        
        return render(request, 'dashboard/manager/cliente/listar_cliente.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/cliente/listar_cliente.html')

@login_required
def administrar_mesas(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/mesas_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/mesas_admin.html')

''' Empleados '''
@login_required
def crear_empleado(request):
    if request.user.is_admin:
        msg=None
        if request.method =='POST':
            form = SignupEmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Usuario creado correctamente'
                return redirect('empleados')
            else:
                msg = 'Error al crear usuario'
        else:
            form = SignupEmployeeForm()
        return render(request, 'dashboard/manager/empleado/crear_empleado.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

    #return render(request, 'dashboard/manager/empleado/crear_empleado.html',{'form':form, 'msg':msg})

@login_required
def empleados(request):
    if request.user.is_admin:
        data = {
            'listado_empleados': 'listar_empleado()'
        }
        return render(request, 'dashboard/manager/empleado/index.html',data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/index.html')

@login_required
def listar_empleado(request):
    if request.user.is_admin:
        connect = connection.cursor()
        db = connect.connection.cursor()
        regresar = connect.connection.cursor()
        db.callproc('SP_LISTAR_MENU', [regresar])
        lista = []
        for fila in regresar:
            data = {
                'data': fila,
            }
            lista.append(data)
        return lista
        #return render(request, 'dashboard/manager/empleado/listar_empleado.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/listar_empleado.html')

@login_required
def modificar_empleado(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/empleado/modificar_empleado.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/modificar_empleado.html')
''' Empleados FIN '''

@login_required
def administrar_reservas(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/reservas_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/reservas_admin.html')

@login_required
def administrar_menu(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/menu_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/menu_admin.html')

@login_required
def administrar_inventario(request):
    if request.user.is_admin:
        return render(request, 'dashboard/manager/inventario.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/inventario.html')

'''----Dashboard - admin - FIN ---'''