# Generated by Django 4.1.1 on 2024-12-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_directorgeneral_especialidad_laboratorio_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
