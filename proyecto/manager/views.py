from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupEmployeeForm, EmployeeForm , MenuForm, TipoMenuForm, MesasForm, TurForm, UsuarioMesaForm
from account.forms import SignupForm
from manager.models import AccountUsuario
from django.db import connection
from account.models import Usuario, Empleado
from .models import  Mesa, Menu, TipoMenu


# Create your views here.

@login_required
def modificar_usuario_mesa(request, id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.method =='POST':
            usuario = Usuario.objects.get(id_usuario=id)
            form = SignupEmployeeForm(request.POST or None,instance=usuario)
            if form.is_valid():
                form.save()
                msg = 'Usuario mesa modificado correctamente'
                return redirect('usuario_mesa')
            else:
                msg = 'Error al modificar el usuario mesa'
        else:
            usuario = Usuario.objects.get(id_usuario=id)
            form = SignupEmployeeForm(instance=usuario)
        return render(request, 'dashboard/manager/usuario_mesa/modificar_usuario_mesa.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)


@login_required
def crear_usuario_mesa(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.method =='POST':
            form = SignupEmployeeForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.is_employee = True
                form.save()
                msg = 'Usuario mesa creado correctamente'
                return redirect('ingresar_usuario_mesa')
            else:
                msg = 'Error al crear Usuario mesa'
        else:
             form = SignupEmployeeForm()
        return render(request, 'dashboard/manager/usuario_mesa/crear.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def ingresar_usuario_mesa(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.POST:
            form = UsuarioMesaForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Usuario mesa ingresado correctamente'
                return redirect('usuario_mesa')
            else:
                msg = 'Error al ingresar el usuario mesa'
        else:
            form = UsuarioMesaForm(request.POST)
        return render(request, 'dashboard/manager/usuario_mesa/ingresar_usuario_mesa.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)


@login_required
def usuario_mesa(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        data = {
            'usr_mesas': listar_usuarios_mesa()
        }
        return render(request, 'dashboard/manager/usuario_mesa/index.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)


def listar_usuarios_mesa():
    with connection.cursor() as cursor:
        cursor.execute("select * from public.fn_listar_usuario_mesa() ")
        out_cur = cursor.fetchall()
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



'''----Dashboard - admin---'''

@login_required
def mod_p_perfil(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        turno = Empleado.objects.get(usuario_id=id)
        form = TurForm(request.POST or None,instance=turno)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('perfil_admin')
        else:
            turno = Empleado.objects.get(usuario_id=id)
            form = TurForm(instance=turno)
        return render(request, 'dashboard/manager/mod_p_perfil.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def perfil_admin(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        return render(request, 'dashboard/manager/perfil_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/perfil_admin.html')

@login_required
def edit_perfil(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        perfil = Usuario.objects.get(id_usuario=id)
        form = SignupEmployeeForm(request.POST or None,instance=perfil)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('perfil_admin')
        else:
            perfil = Usuario.objects.get(id_usuario=id)
            form = SignupEmployeeForm(instance=perfil)
        return render(request, 'dashboard/manager/edit_perfil.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)


def eliminar_cliente(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        cliente = Usuario.objects.get(id_usuario=id)
        cliente.delete()
        return redirect('listar_cliente')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

def listado_clientes():
    emp = Usuario.objects.values('id_usuario','rut','first_name','last_name','email','celular').exclude(is_employee=True).order_by('id_usuario')
    lista = []
    for fila in emp:
        lista.append(fila)
    return lista

@login_required
def modificar_cliente(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        cliente = Usuario.objects.get(id_usuario=id)
        form = SignupForm(request.POST or None,instance=cliente)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('listar_cliente')
        else:
            cliente = Usuario.objects.get(id_usuario=id)
            form = SignupForm(instance=cliente)
        return render(request, 'dashboard/manager/cliente/modificar.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def listar_cliente(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        data = {
            'clientes': listado_clientes()
        }
        return render(request, 'dashboard/manager/cliente/index.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

''' Empleados '''
@login_required
def crear_empleado(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.method =='POST':
            form = SignupEmployeeForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.is_employee = True
                form.save()
                msg = 'Usuario creado correctamente'
                return redirect('ingresar_empleado')
            else:
                msg = 'Error al crear Usuario'
        else:
             form = SignupEmployeeForm()
        return render(request, 'dashboard/manager/empleado/crear_empleado.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)




@login_required
def ingresar_empleado(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.POST:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Empleado ingresado correctamente'
                return redirect('empleados')
            else:
                msg = 'Error al ingresar el Empleado'
        else:
            form = EmployeeForm(request.POST)
        return render(request, 'dashboard/manager/empleado/ingresar_empleado.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)


@login_required
def empleados(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        # empleados = AccountUsuario.objects.exclude(rol= 'is_client' ).values_list('rut','first_name', 'last_name', 'email', 'celular')
        data = {
            'empleados': listado_empleados()
        }
        return render(request, 'dashboard/manager/empleado/index.html',data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/index.html')
    
def listado_empleados():
    with connection.cursor() as cursor:
        cursor.execute("select * from public.fn_listar_empleados() ")
        out_cur = cursor.fetchall()
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista
        # return render(request, 'dashboard/manager/empleado/listado_empleados.html',{'empleados':empleados})
    # else:
    #     msg = {'msg':'No tiene permisos para acceder a esta sección'}
    #     return render(request, 'accounts/request.html', msg)


def eliminar_empleado(request, id):
    empleado = Usuario.objects.get(id_usuario=id)
    empleado.delete()
    return redirect('empleados')

@login_required
def modificar_turno(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        turno = Empleado.objects.get(usuario_id=id)
        form = EmployeeForm(request.POST or None,instance=turno)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('empleados')
        else:
            turno = Empleado.objects.get(usuario_id=id)
            form = EmployeeForm(instance=turno)
        return render(request, 'dashboard/manager/empleado/modificar_turno.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def modificar_empleado(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        empleado = AccountUsuario.objects.get(id_usuario=id)
        form = SignupEmployeeForm(request.POST or None,instance=empleado)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('empleados')
        else:
            empleado = AccountUsuario.objects.get(id_usuario=id)
            form = SignupEmployeeForm(instance=empleado)
        return render(request, 'dashboard/manager/empleado/modificar_empleado.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/empleado/modificar_empleado.html')
''' Empleados FIN '''

@login_required
def administrar_reservas(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        return render(request, 'dashboard/manager/reservas_admin.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def crear_menu(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg = None
        if request.method == 'POST':
            form = MenuForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Menu ingresado correctamente'
                return redirect('administrar_menu')
            else:
                msg = 'Error al ingresar el Menu'
        else:
            form = MenuForm(request.POST)
        return render(request, 'dashboard/manager/menu/crear.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
@login_required
def crear_tipo_menu(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg = None
        if request.method == 'POST':
            form = TipoMenuForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Tipo de Menu ingresado correctamente'
                return redirect('tipos_menus')
            else:
                msg = 'Error al ingresar el Tipo de Menu'
        else:
            form = TipoMenuForm(request.POST)
        return render(request, 'dashboard/manager/menu/tipo_menu.html',{'form':form, 'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def mod_tipos_menus(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        tipo_menu = TipoMenu.objects.get(id_tipo_m=id)
        form = TipoMenuForm(request.POST or None,instance=tipo_menu)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('tipos_menus')
        else:
            tipo_menu = TipoMenu.objects.get(id_tipo_m=id)
            form = TipoMenuForm(instance=tipo_menu)
        return render(request, 'dashboard/manager/menu/mod_tipo_menu.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def modificar_menu(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        menu = Menu.objects.get(id_menu=id)
        form = MenuForm(request.POST or None,instance=menu)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('administrar_menu')
        else:
            menu = Menu.objects.get(id_menu=id)
            form = MenuForm(instance=menu)
        return render(request, 'dashboard/manager/menu/modificar.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

def eliminar_menu(request, id):
    menu = Menu.objects.get(id_menu=id)
    menu.delete()
    return redirect('administrar_menu')

def listado_menu():
    menu = Menu.objects.select_related("id_tipo_m").order_by('id_menu')
    lista = []
    for fila in menu:
        lista.append(fila)
    return lista

def eliminar_tipos_menus(request, id):
    menu = TipoMenu.objects.get(id_tipo_m=id)
    menu.delete()
    return redirect('tipos_menus')

def tipo_menus():
    menu = TipoMenu.objects.values('id_tipo_m','descripcion').order_by('id_tipo_m')
    lista = []
    for fila in menu:
        lista.append(fila)
    return lista

@login_required
def tipos_menus(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        data = {
            'tipos': tipo_menus()
        }
        return render(request, 'dashboard/manager/menu/tipos_menus.html',data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)

@login_required
def administrar_menu(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        data = {
            'menus': listado_menu()
        }
        return render(request, 'dashboard/manager/menu/index.html', data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/menu_admin.html')


@login_required
def administrar_inventario(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        return render(request, 'dashboard/manager/inventario.html')
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/inventario.html')


def eliminar_mesa(request, id):
    mesa = Mesa.objects.get(id_mesa=id)
    mesa.delete()
    return redirect('admin_mesas')


@login_required
def admin_mesas(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        data = {
            'mesas': listar_mesas()
        }
        return render(request, 'dashboard/manager/mesa/index.html',data)
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
    #return render(request, 'dashboard/manager/reservas.html')


def listar_mesas():
    with connection.cursor() as cursor:
        cursor.execute("select * from public.fn_listar_mesas() ")
        out_cur = cursor.fetchall()
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def crear_mesas(request):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        msg=None
        if request.method =='POST':
            form = MesasForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'Mesa creada correctamente'
                return redirect('admin_mesas')
            else:
                msg = 'Error al crear mesa'
        else:
            form = MesasForm()
        return render(request, 'dashboard/manager/mesa/crear.html',{'form':form,'msg':msg})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
        

@login_required
def modificar_mesas(request,id):
    if request.user.is_employee and request.user.empleado.rol == 'Admin':
        mesa = Mesa.objects.get(id_mesa=id)
        form = MesasForm(request.POST or None,instance=mesa)
        if form.is_valid() and request.POST:
            form.save()
            return redirect('admin_mesas')
        else:
            mesa = Mesa.objects.get(id_mesa=id)
            form = MesasForm(instance=mesa)
        return render(request, 'dashboard/manager/mesa/modificar.html',{'form':form})
    else:
        msg = {'msg':'No tiene permisos para acceder a esta sección'}
        return render(request, 'accounts/request.html', msg)
'''----Dashboard - admin - FIN ---'''
