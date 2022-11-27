from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'client/home/index.html')


'''----Dashboard - cliente---'''

def menu(request):
    return render(request, 'dashboard/client/menu.html')

def reservar(request):
    return render(request, 'dashboard/client/reservar.html')

def reservas(request):
    return render(request, 'dashboard/client/reservas.html')

def perfil(request):
    return render(request, 'dashboard/dashboard.html')

'''----Dashboard - cliente - FIN---'''