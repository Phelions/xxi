# Generated by Django 3.2.16 on 2022-12-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
    ]
