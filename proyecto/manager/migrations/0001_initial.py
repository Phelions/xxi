# Generated by Django 3.2.16 on 2022-12-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('email', models.CharField(max_length=100, unique=True)),
                ('rut', models.DecimalField(decimal_places=0, max_digits=9)),
                ('celular', models.DecimalField(decimal_places=0, max_digits=9)),
                ('is_client', models.BooleanField()),
                ('is_admin', models.BooleanField()),
                ('is_finanza', models.BooleanField()),
                ('is_bodega', models.BooleanField()),
                ('is_cocina', models.BooleanField()),
                ('is_barman', models.BooleanField()),
                ('is_garzon', models.BooleanField()),
                ('intentos', models.IntegerField()),
            ],
            options={
                'db_table': 'account_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'account_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'account_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AxesAccessattempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('http_accept', models.CharField(max_length=1025)),
                ('path_info', models.CharField(max_length=255)),
                ('attempt_time', models.DateTimeField()),
                ('get_data', models.TextField()),
                ('post_data', models.TextField()),
                ('failures_since_start', models.IntegerField()),
            ],
            options={
                'db_table': 'axes_accessattempt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AxesAccessfailurelog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('http_accept', models.CharField(max_length=1025)),
                ('path_info', models.CharField(max_length=255)),
                ('attempt_time', models.DateTimeField()),
                ('locked_out', models.BooleanField()),
            ],
            options={
                'db_table': 'axes_accessfailurelog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AxesAccesslog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('http_accept', models.CharField(max_length=1025)),
                ('path_info', models.CharField(max_length=255)),
                ('attempt_time', models.DateTimeField()),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'axes_accesslog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('num_boleta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_garzon', models.CharField(max_length=100)),
                ('fecha_hora', models.CharField(max_length=20)),
                ('detalle_boleta', models.CharField(max_length=1000)),
                ('total_neto', models.DecimalField(decimal_places=0, max_digits=7)),
                ('iva', models.DecimalField(decimal_places=0, max_digits=7)),
                ('propina', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('total', models.DecimalField(decimal_places=0, max_digits=7)),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('hora_entrada', models.CharField(max_length=5)),
                ('hora_salida', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoMesa',
            fields=[
                ('id_est_me', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_mesa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('estado_pedido', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finanza',
            fields=[
                ('id_finanza', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.CharField(max_length=5)),
                ('ingreso', models.IntegerField()),
                ('salida', models.IntegerField()),
                ('ganancia', models.IntegerField()),
            ],
            options={
                'db_table': 'finanza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id_pago', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'forma_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id_insumo', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre_ins', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'insumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_m', models.CharField(max_length=100)),
                ('porcion', models.IntegerField()),
                ('tiempo', models.CharField(blank=True, max_length=5, null=True)),
                ('detalle', models.CharField(max_length=1000)),
                ('precio', models.IntegerField()),
                ('imagen', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id_mesa', models.IntegerField(primary_key=True, serialize=False)),
                ('id_est_me', models.IntegerField()),
                ('capacidad', models.IntegerField()),
            ],
            options={
                'db_table': 'mesa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('id_mesa', models.IntegerField()),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PedidoMenu',
            fields=[
                ('id_relacion', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'pedido_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('correo_proveedor', models.CharField(max_length=100)),
                ('telefono_proveedor', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id_receta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_receta', models.CharField(max_length=100)),
                ('ingredientes', models.CharField(max_length=500)),
                ('preparacion', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'receta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.IntegerField(primary_key=True, serialize=False)),
                ('menaje', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudInsumo',
            fields=[
                ('id_relacion', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'solicitud_insumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoMenu',
            fields=[
                ('id_tipo_m', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.IntegerField(primary_key=True, serialize=False)),
                ('horario', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'turno',
                'managed': False,
            },
        ),
    ]