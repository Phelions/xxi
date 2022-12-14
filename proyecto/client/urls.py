from client.views import perfil,menu, crear_reserva, reservas, index, res_mesa, eliminar_reserva, modificar_reserva
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('pedido/', res_mesa, name='res_mesa'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('reservar/crear/', crear_reserva, name='crear_reserva'),
    path('reserva/eliminar/<int:id>/', eliminar_reserva, name='eliminar_reserva'),
    path('reserva/modificar/<int:id>', modificar_reserva, name='modificar_reserva'),
    path('reservas/', reservas, name='reservas'),
]