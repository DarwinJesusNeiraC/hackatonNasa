# Generated by Django 4.2.6 on 2023-10-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0002_nivelpeligro_habitat_especie_coordenadas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordenadas',
            name='coordenada',
        ),
        migrations.AddField(
            model_name='coordenadas',
            name='latitud',
            field=models.FloatField(default=0.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordenadas',
            name='longitud',
            field=models.FloatField(default=0.4),
            preserve_default=False,
        ),
    ]
