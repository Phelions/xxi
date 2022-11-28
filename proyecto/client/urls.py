from client.views import perfil,menu, reservar, reservas, index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('reservar/', reservar, name='reservar'),
    path('reservas/', reservas, name='reservas'),
]