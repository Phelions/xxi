
from django.urls import path
from manager.views import  perfil_admin, listar_cliente, admin_mesas, crear_empleado, modificar_empleado , administrar_reservas, administrar_menu, administrar_inventario, empleados, eliminar_empleado, crear_mesas, ingresar_empleado, modificar_turno, administrar_menu, crear_menu, crear_tipo_menu, eliminar_mesa, edit_perfil, eliminar_cliente, modificar_cliente, mod_p_perfil, modificar_mesas

urlpatterns = [
    path('perfil_admin/editar/<int:id>',edit_perfil, name='edit_perfil'),
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('perfil_admin/modificar/<int:id>',mod_p_perfil, name='mod_p_perfil'),
    path('cliente/',listar_cliente, name='listar_cliente'),
    path('cliente/eliminar/<int:id>/',eliminar_cliente, name='eliminar_cliente'),
    path('cliente/modificar/<int:id>',modificar_cliente, name='modificar_cliente'),

    path('crear_tipo_menu/',crear_tipo_menu, name='crear_tipo_menu'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('crear_menu/',crear_menu, name='crear_menu'),

    path('mesas/modificar/<int:id>',modificar_mesas, name='modificar_mesas'),
    path('mesas/',admin_mesas, name='admin_mesas'),
    path('mesas/crear/',crear_mesas, name='crear_mesas'),
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