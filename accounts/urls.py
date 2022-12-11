from django.urls import path, include
from . import views
from .views import Register
from django.shortcuts import render

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',Register.as_view(),name='register'),
]