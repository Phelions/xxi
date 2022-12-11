from django.urls import path, include
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.reservar,name='home'),
    path('carrito/',views.carrito,name='carrito'),
    path('boleta/',views.boleta,name='boleta'),
    path('listarreservas/',views.listarreservas,name='listarreservas'),
    path('eliminar_reserva/<id_reserva>/',views.eliminar_reserva,name='eliminar_reserva'),
    path('agregar/<int:id_menu>/', views.agregar_menu_carrito, name="Add"),
    path('eliminar/<int:id_menu>/', views.eliminar_menu_carrito, name="Del"),
    path('restar/<int:id_menu>/', views.restar_menu_carrito, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    #path('mandar_pedido/', views.mandar_pedidos, name="mandar"),
    path('menu/',views.menu,name='menu'),
    path('mesa/',views.mesa,name='mesa'),
    path('update_mesa/<id_mesa>/', views.update_mesa, name='update_mesa'),
    
]