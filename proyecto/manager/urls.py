
from django.urls import path
from manager.views import  perfil_admin, listar_cliente, admin_mesas, crear_empleado, modificar_empleado , administrar_reservas, administrar_menu, administrar_inventario, empleados, eliminar_empleado, crear_mesas, ingresar_empleado, modificar_turno, administrar_menu, crear_menu, crear_tipo_menu, eliminar_mesa, edit_perfil, eliminar_cliente, modificar_cliente, mod_p_perfil, modificar_mesas, eliminar_menu,tipos_menus, eliminar_tipos_menus, modificar_menu, mod_tipos_menus, usuario_mesa, crear_usuario_mesa, ingresar_usuario_mesa, modificar_usuario_mesa

urlpatterns = [
    path('usuario_mesa/ingresar/',ingresar_usuario_mesa, name='ingresar_usuario_mesa'),
    path('usuario_mesa/crear/',crear_usuario_mesa, name='crear_usuario_mesa'),
    path('usuario_mesa/',usuario_mesa, name='usuario_mesa'),
    path('usuario_mesa/modificar/<int:id>',modificar_usuario_mesa, name='modificar_usuario_mesa'),

    path('perfil_admin/editar/<int:id>',edit_perfil, name='edit_perfil'),
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('perfil_admin/modificar/<int:id>',mod_p_perfil, name='mod_p_perfil'),
    path('cliente/',listar_cliente, name='listar_cliente'),
    path('cliente/eliminar/<int:id>/',eliminar_cliente, name='eliminar_cliente'),
    path('cliente/modificar/<int:id>',modificar_cliente, name='modificar_cliente'),

    path('administrar_menu/crear_tipo_menu/',crear_tipo_menu, name='crear_tipo_menu'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('administrar_menu/crear/',crear_menu, name='crear_menu'),
    path('administrar_menu/modificar_tipo_menu/<int:id>',mod_tipos_menus, name='mod_tipos_menus'),
    path('administrar_menu/modificar/<int:id>',modificar_menu, name='modificar_menu'),
    path('administrar_menu/eliminar/<int:id>',eliminar_menu, name='eliminar_menu'),
    path('administrar/menu/tipos_menus/',tipos_menus, name='tipos_menus'),
    path('administrar/menu/tipos_menus/eliminar/<int:id>',eliminar_tipos_menus, name='eliminar_tipos_menus'),

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