from . import views
from django.urls import path
from manager.views import  perfil_admin, listar_cliente, admin_mesas, crear_empleado, modificar_empleado , administrar_reservas, administrar_menu, administrar_inventario, empleados, eliminar_empleado, crear_mesas, agregar_empleado

urlpatterns = [ 
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('listar_cliente/',listar_cliente, name='listar_cliente'),

    path('mesas/',admin_mesas, name='mesas'),
    path('mesas/crear/',crear_mesas, name='crear'),
    
    path('agregar_empleado/',agregar_empleado, name='agregar_empleado'),
    path('crear_empleado/',crear_empleado, name='crear_empleado'),
    path('empleado/modificar/<int:id>',modificar_empleado, name='modificar'),
    path('empleados/',empleados, name='empleados'),
    path('eliminar/',eliminar_empleado, name='eliminar'),


    path('administrar_reservas/',administrar_reservas, name='administrar_reservas'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('administrar_inventario/',administrar_inventario, name='administrar_inventario'),
]