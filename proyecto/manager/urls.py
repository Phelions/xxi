from . import views
from django.urls import path
from manager.views import  perfil_admin, listar_cliente, administrar_mesas, crear_empleado, modificar_empleado ,listar_empleado, administrar_reservas, administrar_menu, administrar_inventario, empleados, eliminar_empleado

urlpatterns = [ 
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('listar_cliente/',listar_cliente, name='listar_cliente'),
    path('administrar_mesas/',administrar_mesas, name='administrar_mesas'),
    
    path('crear_empleado/',crear_empleado, name='crear_empleado'),
    path('listar_empleado/',listar_empleado, name='listar_empleado'),
    path('modificar_empleado/',modificar_empleado, name='modificar_empleado'),
    path('empleados/',empleados, name='empleados'),
    path('eliminar/<int:rut>',eliminar_empleado, name='eliminar'),


    path('administrar_reservas/',administrar_reservas, name='administrar_reservas'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('administrar_inventario/',administrar_inventario, name='administrar_inventario'),
]