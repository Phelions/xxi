# Generated by Django 3.2.16 on 2022-12-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_estadosolicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmpleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(blank=True, max_length=7, null=True)),
                ('turno', models.CharField(blank=True, max_length=9, null=True)),
                ('hora_entrada', models.DateTimeField(blank=True, null=True)),
                ('hora_salida', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountUsuario',
            fields=[
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('rut', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('celular', models.IntegerField()),
                ('is_client', models.BooleanField()),
                ('is_employee', models.BooleanField()),
                ('intentos', models.IntegerField()),
            ],
            options={
                'db_table': 'account_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountUsuarioGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'account_usuario_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountUsuarioUserPermi783D',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'account_usuario_user_permi783d',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_det_ped', models.BigIntegerField(primary_key=True, serialize=False)),
                ('detalle_ped', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'detalle_pedido',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AccountUser',
        ),
        migrations.DeleteModel(
            name='AccountUserGroups',
        ),
        migrations.DeleteModel(
            name='AccountUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='EstadoSolicitud',
        ),
        migrations.DeleteModel(
            name='Turno',
        ),
    ]
