from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class Usuario(models.Model):
    rut = models.PositiveIntegerField(default=9, validators=[MinValueValidator(9), MaxValueValidator(9)], primary_key=True,null=False)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    celular = models.PositiveIntegerField(default=9, validators=[MinValueValidator(9), MaxValueValidator(9)],null=False)
    email = models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=12,null=False)

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255,null=False)
    tabla_afectada = models.CharField(max_length=50,null=False)
    fecha_hora = models.DateTimeField(null=False)

class Turno(models.Model):
    horario = models.CharField(max_length=255,null=False)

class Tipo_empleado(models.Model):
    nombre_rol = models.CharField(max_length=20,null=False)

class Empleado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_empleado = models.ForeignKey(Tipo_empleado, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(null=False)
    fecha_termino = models.DateField(null=False)

    def __str__(self):
        return self.usuario.nombre
