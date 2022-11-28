from django.shortcuts import render

# Create your views here.



'''----Dashboard - admin---'''

def perfil_admin(request):
    return render(request, 'dashboard/manager/perfil_admin.html')

def administrar_clientes(request):
    return render(request, 'dashboard/manager/clientes_admin.html')

def administrar_mesas(request):
    return render(request, 'dashboard/manager/mesas_admin.html')

def administrar_empleados(request):
    return render(request, 'dashboard/manager/empleados_admin.html')

def administrar_reservas(request):  
    return render(request, 'dashboard/manager/reservas_admin.html')

def administrar_menu(request):
    return render(request, 'dashboard/manager/menu_admin.html')

def administrar_inventario(request):
    return render(request, 'dashboard/manager/inventario.html')

'''----Dashboard - admin - FIN ---'''