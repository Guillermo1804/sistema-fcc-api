# Generated by Django 5.0.2 on 2024-04-22 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_fcc_api', '0007_rename_area_maestros_area_investigacion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestros',
            name='edad',
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nrc', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('seccion', models.CharField(blank=True, max_length=255, null=True)),
                ('materias_dia', models.TextField(blank=True, null=True)),
                ('horario_inicio', models.DateTimeField(blank=True, null=True)),
                ('horario_final', models.DateTimeField(blank=True, null=True)),
                ('salon', models.CharField(blank=True, max_length=255, null=True)),
                ('programa', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]