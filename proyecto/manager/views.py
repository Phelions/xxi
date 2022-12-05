from django.shortcuts import render, redirect
from account.forms import SignupEmployeeForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import AccountUser, Empleado, Turno
from django.db.models import fields
from django.db.models import F
from django.db.models import Case, When, Value
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
        #qs1 =  Empleado.objects.values_list('hora_entrada','hora_salida')
        #qs2 =  Turno.objects.values_list('horario')
        
        empleados = AccountUser.objects.select_related('empleado','turno').annotate(
            rol=Case(
                When(is_admin=True, then=Value('Admin')),
                When(is_bodega=True, then=Value('Bodega')),
                When(is_finanza=True, then=Value('Finanza')),
                When(is_cocina=True, then=Value('Cocina')),
                When(is_barman=True, then=Value('Barman')),
                When(is_garzon=True, then=Value('Garzón')),
            ), 
        ).exclude(rol= 'is_client' ).values_list('rut','first_name', 'last_name', 'email', 'celular', 'rol')
        return render(request, 'dashboard/manager/empleado/index.html',{'empleados':empleados})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/index.html')

@login_required
def listar_empleado(request):
    if request.user.is_admin:
        # django_cursor = connection.cursor()
        # cursor = django_cursor.connection.cursor()
        # out_cur = django_cursor.connection.cursor()
        # cursor.callproc('sp_listar_empleados', [out_cur])
        # lista = []
        # for fila in out_cur:
        #     lista.append(fila)
        # return lista
        
        
    # query = "SELECT rut, first_name, last_name, email, celular,CASE WHEN is_admin='true' then 'Admin'WHEN is_bodega='true' then 'Bodega' WHEN is_finanza='true' then 'Finanza' WHEN is_cocina='true' then 'Cocina' WHEN is_barman='true' then 'Barman'WHEN is_garzon='true' then 'Garzón' end AS rol, hora_entrada, hora_salida, horario FROM account_user FULL JOIN empleado ON account_user.id=empleado.id_usuario FULL JOIN turno ON turno.id_turno=empleado.id_turno WHERE NOT is_client"
    # cursor = connection.cursor()
    # cursor.execute(query)
    # cursor.fetchall()
    # lista = []
    # for fila in cursor.fetchall():
    #     p = (fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
    #     lista.append(p)
    # return lista


        return render(request, 'dashboard/manager/empleado/listar_empleado.html')
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