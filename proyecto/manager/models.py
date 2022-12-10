
from django.db import models


class AccountEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=7, blank=True, null=True)
    turno = models.CharField(max_length=9, blank=True, null=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    usuario = models.OneToOneField('AccountUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_empleado'


class AccountUsuario(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    rut = models.IntegerField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    celular = models.IntegerField()
    is_client = models.BooleanField()
    is_employee = models.BooleanField()
    intentos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_usuario'


class AccountUsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AccountUsuario, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_usuario_groups'
        unique_together = (('usuario', 'group'),)


class AccountUsuarioUserPermi783D(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AccountUsuario, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_usuario_user_permi783d'
        unique_together = (('usuario', 'permission'),)


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


class AxesAccessattempt(models.Model):
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025, blank=True, null=True)
    path_info = models.CharField(max_length=255, blank=True, null=True)
    attempt_time = models.DateTimeField()
    get_data = models.TextField(blank=True, null=True)
    post_data = models.TextField(blank=True, null=True)
    failures_since_start = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'axes_accessattempt'
        unique_together = (('username', 'ip_address', 'user_agent'),)


class AxesAccessfailurelog(models.Model):
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025, blank=True, null=True)
    path_info = models.CharField(max_length=255, blank=True, null=True)
    attempt_time = models.DateTimeField()
    locked_out = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'axes_accessfailurelog'


class AxesAccesslog(models.Model):
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=1025, blank=True, null=True)
    path_info = models.CharField(max_length=255, blank=True, null=True)
    attempt_time = models.DateTimeField()
    logout_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axes_accesslog'


class Boleta(models.Model):
    num_boleta = models.BigIntegerField(primary_key=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido')
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
    user = models.ForeignKey(AccountUsuario, models.DO_NOTHING)

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


class EstadoMesa(models.Model):
    id_est_me = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_mesa'
    def __str__(self):
        return self.descripcion

class EstadoPedido(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Finanza(models.Model):
    id_finanza = models.BigIntegerField(primary_key=True)
    id_empleado = models.BigIntegerField()
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
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_empleado = models.BigIntegerField()
    codigo = models.CharField(max_length=10)
    nombre_ins = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'insumo'


class Menu(models.Model):
    id_menu = models.BigIntegerField(primary_key=True)
    id_tipo_m = models.ForeignKey('TipoMenu', models.DO_NOTHING, db_column='id_tipo_m')
    nombre_m = models.CharField(max_length=50)
    porcion = models.BigIntegerField()
    tiempo = models.CharField(max_length=5)
    detalle = models.CharField(max_length=255)
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu'


class Mesa(models.Model):
    id_mesa = models.OneToOneField(AccountEmpleado, models.DO_NOTHING, db_column='id_mesa', primary_key=True)
    id_est_me = models.ForeignKey(EstadoMesa, models.DO_NOTHING, db_column='id_est_me')
    capacidad = models.BigIntegerField()
    id_empleado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesa'
    def __str__(self):
        return self.id_est_me.descripcion

class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    id_estado = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado')
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoMenu(models.Model):
    id_pedido = models.OneToOneField(Pedido, models.DO_NOTHING, db_column='id_pedido', primary_key=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_menu'
        unique_together = (('id_pedido', 'id_menu'),)


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    correo_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    id_receta = models.BigIntegerField(primary_key=True)
    id_empleado = models.BigIntegerField()
    nombre_receta = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    preparacion = models.CharField(max_length=2000)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu')

    class Meta:
        managed = False
        db_table = 'receta'


class Reserva(models.Model):
    id_reserva = models.OneToOneField(AccountUsuario, models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='id_mesa')
    fecha_hora = models.CharField(max_length=20)
    id_usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reserva'


class Solicitud(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    id_empleado = models.BigIntegerField()
    mensaje = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'solicitud'


class SolicitudInsumo(models.Model):
    id_solicitud = models.OneToOneField(Solicitud, models.DO_NOTHING, db_column='id_solicitud', primary_key=True)
    id_insumo = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='id_insumo')
    cantidad_soli = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'solicitud_insumo'
        unique_together = (('id_solicitud', 'id_insumo'),)


class TipoMenu(models.Model):
    id_tipo_m = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_menu'