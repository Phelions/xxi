from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Usuario(models.Model):
    rut = models.PositiveIntegerField(default=9, validators=[MinValueValidator(9), MaxValueValidator(9)], primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.PositiveIntegerField(default=9, validators=[MinValueValidator(9), MaxValueValidator(9)])
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    tabla_afectada = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField()

class Turno(models.Model):
    horario = models.CharField(max_length=255)

class Empleado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()

    def __str__(self):
        return self.usuario.nombre
