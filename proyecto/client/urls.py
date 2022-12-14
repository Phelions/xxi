from client.views import perfil,menu, crear_reserva, reservas, index, res_mesa, agregar_pedido, crear_pedido, eliminar_pedido_menu
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('pedido/', res_mesa, name='res_mesa'),
    path('pedido/agregar/<int:id_menu>', agregar_pedido, name='agregar_pedido'),
    path('pedido/crear/', crear_pedido, name='crear_pedido'),
    path('pedido/eliminar/<int:id_menu>', eliminar_pedido_menu, name='eliminar_pedido_menu'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('reservar/crear/', crear_reserva, name='crear_reserva'),
    path('reservas/', reservas, name='reservas'),
]