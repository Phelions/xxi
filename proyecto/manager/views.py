from django.shortcuts import render, redirect
from account.forms import SignupEmployeeForm
from django.contrib.auth.decorators import login_required
from .models import AccountUser, Empleado, Turno
import hashlib
from account.forms import EmpleadoForm
from .forms import MesaForm
from django.db.models import Case, When, Value
from account.models import User
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

@login_required
def crear_mesas(request):
    if request.user.is_admin:
        msg=None
        if request.method =='POST':
            form = MesaForm(request.POST)
            if form.is_valid():
                
                form.save()
                msg = 'Mesa creada correctamente'
                return redirect('mesas')
            else:
                msg = 'Error al crear mesa'
        else:
            form = MesaForm()
        return render(request, 'dashboard/manager/mesa/crear.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

''' Empleados '''
@login_required
def crear_empleado(request):
    if request.user.is_admin:
        msg=None
        data = {
            'turnos': listar_turno(),
        }
        return render(request, 'dashboard/manager/empleado/crear_empleado.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def agregar_empleado(request):
    if request.user.is_admin:
        msg=None
        if request.method =='POST':
            
            # Tabla Account_user
            con = request.POST.get('password1')
            h = hashlib.md5(con.encode())
            contrasena = h.hexdigest()
            nombre = request.POST.get('first_name')
            apellido = request.POST.get('last_name')
            correo = request.POST.get('email')
            rut = request.POST.get('rut')
            celular = request.POST.get('celular')
            es_admin = request.POST.get('is_admin')
            es_finanza = request.POST.get('is_finanza')
            es_bodega = request.POST.get('is_bodega')
            es_cocina = request.POST.get('is_cocina')
            es_barman = request.POST.get('is_barman')
            es_garzon = request.POST.get('is_garzon')
            
            # Tabla Empleado
            id_turno = request.POST.get('turno_box')
            hora_entrada = request.POST.get('hora_entrada')
            hora_salida = request.POST.get('hora_salida')
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO account_user (password, is_superuser, first_name, last_name, is_staff, is_active, email, rut, celular, username, intentos, is_client, is_admin, is_finanza, is_bodega, is_cocina, is_barman, is_garzon) VALUES ('"+contrasena+"', 'false', '"+nombre+"', '"+apellido+"', 'true', 'true', '"+correo+"', '"+rut+"', '"+celular+"', Null, 0, 'false', '"+es_admin+"', '"+es_finanza+"', '"+es_bodega+"', '"+es_cocina+"', '"+es_barman+"', '"+es_garzon+"')")
                cursor.execute("INSERT INTO empleado (id_usuario, id_turno, hora_entrada, hora_salida) VALUES (currval('account_user_id_seq'), '"+id_turno+"', '"+hora_entrada+"', '"+hora_salida+"')")
                msg = {'msg':'Empleado creado correctamente'}
                return redirect('empleados')
        else:
            msg = {'msg':'Error al crear empleado'}
            return render(request, 'dashboard/manager/empleado/crear_empleado.html', msg)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
            


def listar_empleados():
    with connection.cursor() as cursor:
        cursor.execute("SELECT em.id_empleado, au.rut, au.first_name, au.last_name, au.email, au.celular, CASE WHEN au.is_admin='true' then 'Admin' WHEN au.is_bodega='true' then 'Bodega' WHEN au.is_finanza='true' then 'Finanza' WHEN au.is_cocina='true' then 'Cocina' WHEN au.is_barman='true' then 'Barman' WHEN au.is_garzon='true' then 'Garzón' end AS rol, em.hora_entrada, em.hora_salida, tu.horario FROM empleado em JOIN account_user au ON au.id = em.id_usuario JOIN turno tu ON em.id_turno = tu.id_turno where not au.is_client")
        out_cur = cursor.fetchall()
                
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista

def listar_turno():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_turno, horario FROM turno")
        out_cur = cursor.fetchall()
                
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista

@login_required
def empleados(request):
    if request.user.is_admin:
        # empleados = AccountUser.objects.annotate(
        #     rol=Case(
        #         When(is_admin=True, then=Value('Admin')),
        #         When(is_bodega=True, then=Value('Bodega')),
        #         When(is_finanza=True, then=Value('Finanza')),
        #         When(is_cocina=True, then=Value('Cocina')),
        #         When(is_barman=True, then=Value('Barman')),
        #         When(is_garzon=True, then=Value('Garzón')),
        #     ), 
        # ).exclude(rol= 'is_client' ).values_list('rut','first_name', 'last_name', 'email', 'celular', 'rol')
        
        # empleado = AccountUser.objects.raw('''SELECT em.id_empleado as id, au.rut as rut, au.first_name as first_name, au.last_name as last_name, au.email as email, au.celular as celular, CASE WHEN au.is_admin='true' then 'Admin' WHEN au.is_bodega='true' then 'Bodega' WHEN au.is_finanza='true' then 'Finanza' WHEN au.is_cocina='true' then 'Cocina' WHEN au.is_barman='true' then 'Barman' WHEN au.is_garzon='true' then 'Garzón' end AS rol, em.hora_entrada as hora_entrada, em.hora_salida as hora_salida, tu.horario as horario FROM empleado em JOIN account_user au ON au.id = em.id_usuario JOIN turno tu ON em.id_turno = tu.id_turno where not au.is_client;''')
        # empleados = empleado.columns
        
        data = {
            'empleados': listar_empleados(),
        }
        
        return render(request, 'dashboard/manager/empleado/index.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/index.html')


def eliminar_empleado(request, rut):
    empleado = AccountUser.objects.get(rut=rut)
    empleado.delete()
    return redirect('empleados')


@login_required
def modificar_empleado(request,rut):
    if request.user.is_admin:
        empleado = User.objects.get(rut=rut)
        form = EmpleadoForm(request.POST or None,instance=empleado)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('empleados')
        else:
            empleado = User.objects.get(rut=rut)
            form = EmpleadoForm(instance=empleado)
        return render(request, 'dashboard/manager/empleado/modificar_empleado.html',{'form':form})
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


@login_required
def admin_mesas(request):
    if request.user.is_admin:

        return render(request, 'dashboard/manager/mesa/index.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/reservas.html')


'''----Dashboard - admin - FIN ---'''