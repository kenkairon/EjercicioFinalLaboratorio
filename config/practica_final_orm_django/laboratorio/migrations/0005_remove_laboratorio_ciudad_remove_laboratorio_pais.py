# Generated by Django 4.1.1 on 2025-02-03 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0004_alter_laboratorio_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='laboratorio',
            name='pais',
        ),
    ]
