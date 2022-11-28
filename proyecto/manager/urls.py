from . import views
from django.urls import path
from manager.views import  perfil_admin, administrar_clientes, administrar_mesas, administrar_empleados, administrar_reservas, administrar_menu, administrar_inventario

urlpatterns = [ 
    path('perfil_admin/',perfil_admin, name='perfil_admin'),
    path('administrar_clientes/',administrar_clientes, name='administrar_clientes'),
    path('administrar_mesas/',administrar_mesas, name='administrar_mesas'),
    path('administrar_empleados/',administrar_empleados, name='administrar_empleados'),
    path('administrar_reservas/',administrar_reservas, name='administrar_reservas'),
    path('administrar_menu/',administrar_menu, name='administrar_menu'),
    path('administrar_inventario/',administrar_inventario, name='administrar_inventario'),
]