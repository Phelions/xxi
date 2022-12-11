# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsUsuario(models.Model):
    contrasena = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    id_usuario = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=9, blank=True, null=True)
    usuario_administrador = models.BooleanField()
    usuario_activo = models.BooleanField()
    usuario_empleado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'accounts_usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
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
    num_boleta = models.BigIntegerField(primary_key=True)
    id_mesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='id_mesa')
    nombre_garzon = models.CharField(max_length=100)
    fecha_hora = models.CharField(max_length=20)
    detalle_boleta = models.CharField(max_length=1000)
    id_forma_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='id_forma_pago')
    total_neto = models.IntegerField()
    iva = models.IntegerField()
    propina = models.IntegerField(blank=True, null=True)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'boleta'


class DetallePedido(models.Model):
    id_det_ped = models.BigIntegerField(primary_key=True)
    detalle_ped = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.BigIntegerField(primary_key=True)
    id_rol = models.ForeignKey('TipoRol', models.DO_NOTHING, db_column='id_rol')
    id_turno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='id_turno')
    id_usuario = models.BigIntegerField()
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoMesa(models.Model):
    id_est_me = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_mesa'


class EstadoPedido(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Finanza(models.Model):
    id_finanza = models.BigIntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    num_boleta = models.BigIntegerField()
    fecha = models.CharField(max_length=25)
    ingreso = models.BigIntegerField()
    salida = models.BigIntegerField()
    ganancia = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'finanza'


class FormaPago(models.Model):
    id_pago = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Insumo(models.Model):
    id_insumo = models.BigIntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    codigo = models.CharField(max_length=10)
    nombre_ins = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insumo'


class Menu(models.Model):
    id_menu = models.BigIntegerField(primary_key=True)
    nombre_m = models.CharField(max_length=50)
    porcion = models.BigIntegerField()
    detalle = models.CharField(max_length=255)
    precio = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'menu'


class Mesa(models.Model):
    id_mesa = models.BigIntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    id_est_me = models.ForeignKey(EstadoMesa, models.DO_NOTHING, db_column='id_est_me')

    class Meta:
        managed = False
        db_table = 'mesa'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')
    id_estado = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado')
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class Receta(models.Model):
    id_receta = models.BigIntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    nombre_receta = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    preparacion = models.CharField(max_length=2000)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')

    class Meta:
        managed = False
        db_table = 'receta'


class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    id_usuario = models.BigIntegerField()
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    fecha_hora = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'reserva'


class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    mensaje = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'solicitud'


class TipoRol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_rol'


class Turno(models.Model):
    id_turno = models.BigIntegerField(primary_key=True)
    horario = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'turno'
