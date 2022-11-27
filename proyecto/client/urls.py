from . import views
from client.views import perfil,menu, reservar, reservas
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
    path('reservar/', reservar, name='reservar'),
    path('reservas/', reservas, name='reservas'),
]