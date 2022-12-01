from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.CharField("Correo",unique=True, max_length=100)
    rut = models.DecimalField(max_digits=9, decimal_places=0)
    celular = models.DecimalField(max_digits=9, decimal_places=0)
    is_client = models.BooleanField('Rol cliente',default=True)
    is_admin = models.BooleanField('Rol admin',default=False)
    is_finanza = models.BooleanField('Rol finanza',default=False)
    is_bodega = models.BooleanField('Rol bodega',default=False)
    is_cocina = models.BooleanField('Rol cocina',default=False)
    is_barman = models.BooleanField('Rol barman',default=False)
    is_garzon = models.BooleanField('Rol garzon',default=False)


    REQUIRED_FIELDS = ['rut', 'first_name', 'last_name','username','celular']
    USERNAME_FIELD = 'email'
