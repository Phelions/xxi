from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/',views.dashboard,name='dashboard'),
    path('mesa/',views.list_menu,name='list_menu'),

]