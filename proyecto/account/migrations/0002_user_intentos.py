# Generated by Django 3.2.16 on 2022-12-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intentos',
            field=models.IntegerField(default=0),
        ),
    ]
