from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField( max_length=100, unique=False, blank=True, null=True)
    rut = models.PositiveIntegerField()
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)
    email = models.CharField("Correo",unique=True, max_length=100)
    celular = models.PositiveIntegerField()
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    intentos = models.IntegerField(default=0)


    REQUIRED_FIELDS = ['rut', 'first_name', 'last_name','username', 'celular']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.first_name + " " + self.last_name
        
    class Meta:
        managed = True
        verbose_name = 'Usuario'

    
TURNO = [
    ('Part-Time', 'Part-Time'),
    ('Full-Time', 'Full-Time'),
]

ROL = [
    ('Admin', 'Admin'),
    ('Finanza', 'Finanza'),
    ('Mesa', 'Mesa'),
    ('Bodega', 'Bodega'),
    ('Cocina', 'Cocina'),
    ('Barman', 'Barman'),
    ('Garzon', 'Garzon'),
    
]

class Empleado(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empleado')
    id_empleado = models.AutoField(primary_key=True)
    rol = models.CharField(choices=ROL,max_length=7)
    turno = models.CharField(choices=TURNO, max_length=9)
    hora_entrada = models.TimeField(null=True)
    hora_salida = models.TimeField(null=True)
    
    class Meta:
        managed = True
        verbose_name = 'Empleado'
        
    def __str__(self):
        return self.usuario.first_name + " " + self.usuario.last_name + " - " + self.rol
