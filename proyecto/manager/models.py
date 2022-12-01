# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    num_boleta = models.IntegerField(primary_key=True)
    id_mesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='id_mesa')
    nombre_garzon = models.CharField(max_length=100)
    fecha_hora = models.CharField(max_length=20)
    detalle_boleta = models.CharField(max_length=1000)
    id_forma_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='id_forma_pago')
    total_neto = models.DecimalField(max_digits=7, decimal_places=0)
    iva = models.DecimalField(max_digits=7, decimal_places=0)
    propina = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'boleta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_turno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='id_turno')
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoMesa(models.Model):
    id_est_me = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_mesa'


class EstadoPedido(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Finanza(models.Model):
    id_finanza = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    num_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='num_boleta')
    fecha_hora = models.CharField(max_length=5)
    ingreso = models.IntegerField()
    salida = models.IntegerField()
    ganancia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'finanza'


class FormaPago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Insumo(models.Model):
    id_insumo = models.IntegerField(primary_key=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    codigo = models.CharField(max_length=10)
    nombre_ins = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'insumo'


class Menu(models.Model):
    id_menu = models.IntegerField(primary_key=True)
    id_tipo_m = models.ForeignKey('TipoMenu', models.DO_NOTHING, db_column='id_tipo_m')
    nombre_m = models.CharField(max_length=100)
    porcion = models.IntegerField()
    tiempo = models.CharField(max_length=5, blank=True, null=True)
    detalle = models.CharField(max_length=1000)
    precio = models.IntegerField()
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Mesa(models.Model):
    id_mesa = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_est_me = models.IntegerField()
    capacidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesa'


class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado')
    id_mesa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoMenu(models.Model):
    id_relacion = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_menu'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    correo_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    id_receta = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')
    nombre_receta = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    preparacion = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'receta'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    fecha_hora = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'reserva'


class Solicitud(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    menaje = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'solicitud'


class SolicitudInsumo(models.Model):
    id_relacion = models.IntegerField(primary_key=True)
    id_solicitud = models.ForeignKey(Solicitud, models.DO_NOTHING, db_column='id_solicitud')
    id_insumo = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='id_insumo')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'solicitud_insumo'


class TipoMenu(models.Model):
    id_tipo_m = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_menu'


class TipoRol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_rol'
    def __str__(self):
        return f"{self.id_rol} - {self.descripcion}"

class Turno(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    horario = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'turno'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(TipoRol, models.DO_NOTHING, db_column='id_rol')
    rut = models.DecimalField(max_digits=9, decimal_places=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.DecimalField(max_digits=9, decimal_places=0)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=12)
    activo = models.BooleanField()
    intentos = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nombre}  {self.apellido} | RUT: {self.rut}"