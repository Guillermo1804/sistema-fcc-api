# Generated by Django 5.0.2 on 2024-03-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_fcc_api', '0003_rename_profiles_maestros'),
    ]

    operations = [
        migrations.AddField(
            model_name='maestros',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='confirmar_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='cubiculo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='curp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='fecha_nacimiento',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='id_trabajador',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='materias_json',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='maestros',
            name='rfc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
