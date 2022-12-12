from client.views import perfil,menu, crear_reserva, reservas, index, res_mesa
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('mesa_uno/', res_mesa, name='res_mesa'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('reservar/crear/', crear_reserva, name='crear_reserva'),
    path('reservas/', reservas, name='reservas'),
]