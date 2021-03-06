# Generated by Django 2.1.3 on 2019-03-11 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profesor', '0002_auto_20190118_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccionprofesor',
            options={'ordering': ('region', 'provincia', 'comuna'), 'verbose_name': 'Direccion', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ('nombre', 'apellido_pat'), 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterModelOptions(
            name='tipo_grado',
            options={'ordering': ('profesor', 'nombre_tipo'), 'verbose_name': 'Grado', 'verbose_name_plural': 'Grados'},
        ),
    ]
