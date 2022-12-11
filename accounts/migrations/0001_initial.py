# Generated by Django 3.2.16 on 2022-11-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=9, null=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_empleado', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
