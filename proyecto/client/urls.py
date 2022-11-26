from . import views
from client.views import perfil,dashboard
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('dashboard/', dashboard, name='dashboard'),
]