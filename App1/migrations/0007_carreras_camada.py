# Generated by Django 4.1.5 on 2023-02-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_remove_carreras_camada'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreras',
            name='camada',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
