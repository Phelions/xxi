from client.views import perfil,menu, crear_reserva, reservas, index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('reservas/', reservas, name='reservas'),
]