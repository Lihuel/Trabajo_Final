# Generated by Django 4.2.1 on 2023-05-29 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_equipo_delete_liga'),
        ('jugador', '0003_jugador_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo'),
        ),
    ]
