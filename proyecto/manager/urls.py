
from django.urls import path
from manager.views import  perfil_admin, listar_cliente, admin_mesas, crear_empleado, modificar_empleado , administrar_reservas, administrar_menu, administrar_inventario, empleados, eliminar_empleado, crear_mesas, ingresar_empleado, modificar_turno, administrar_menu, crear_menu, crear_tipo_menu, eliminar_mesa

urlpatterns = [
    
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('listar_cliente/',listar_cliente, name='listar_cliente'),

    path('crear_tipo_menu/',crear_tipo_menu, name='crear_tipo_menu'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('crear_menu/',crear_menu, name='crear_menu'),
    path('mesas/',admin_mesas, name='mesas'),
    path('mesas/crear/',crear_mesas, name='crear'),
    path('mesas/eliminar/<int:id>/',eliminar_mesa, name='eliminar_mesa'),
    
    path('crear_empleado/',crear_empleado, name='crear_empleado'),
    path('ingresar_empleado/',ingresar_empleado, name='ingresar_empleado'),
    path('empleado/modificar/<int:id>',modificar_empleado, name='modificar'),
    path(r'^empleado/modificar_turno/(?P<id>[0-9]+)/$',modificar_turno, name='modificar_turno'),
    path('empleados/',empleados, name='empleados'),
    path('eliminar/<int:id>/',eliminar_empleado, name='eliminar'),


    path('administrar_reservas/',administrar_reservas, name='administrar_reservas'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('administrar_inventario/',administrar_inventario, name='administrar_inventario'),
]