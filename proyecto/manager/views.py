from django.shortcuts import render, redirect
from account.forms import SignupEmployeeForm
from django.contrib.auth.decorators import login_required
from .models import AccountUser, Empleado, Turno
from django.shortcuts import get_list_or_404, get_object_or_404
from account.forms import EmpleadoForm
from .forms import MesaForm
from django.db.models import Case, When, Value
from account.models import User

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

@login_required
def empleados(request):
    if request.user.is_admin:
        empleados = AccountUser.objects.annotate(
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