from django.db import models

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    rut = models.DecimalField(max_digits=9, decimal_places=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.DecimalField(max_digits=9, decimal_places=0)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=12)
    es_admin = models.DecimalField(max_digits=1, decimal_places=0)
    es_empleado = models.DecimalField(max_digits=1, decimal_places=0)
    activo = models.DecimalField(max_digits=1, decimal_places=0)
    intentos = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'usuario'
        
class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255,null=False)
    tabla_afectada = models.CharField(max_length=50,null=False)
    fecha_hora = models.DateTimeField(null=False)        



class Turno(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    horario = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'turno'



class TipoRol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_rol'
