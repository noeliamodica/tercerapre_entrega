# Generated by Django 4.1.5 on 2023-02-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_rename_profedores_profesores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carreras',
            old_name='duracion',
            new_name='camada',
        ),
    ]
