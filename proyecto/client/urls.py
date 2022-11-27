from . import views
from client.views import perfil,menu
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('menu/', menu, name='menu'),
]