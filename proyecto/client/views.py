from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'client/home/index.html')

def dashboard(request):
    return render(request, 'dashboard/base.html')

def perfil(request):
    return render(request, 'dashboard/dashboard.html')