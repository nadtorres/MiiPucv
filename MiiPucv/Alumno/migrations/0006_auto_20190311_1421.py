# Generated by Django 2.1.3 on 2019-03-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0005_auto_20190307_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'ordering': ('nombre',), 'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelOptions(
            name='cursos_homologados',
            options={'ordering': ('nombre',), 'verbose_name': 'Cursos_homologado', 'verbose_name_plural': 'Cursos_homologados'},
        ),
        migrations.AlterModelOptions(
            name='direccionalumno',
            options={'ordering': ('region', 'provincia', 'comuna'), 'verbose_name': 'Direccion_alumno', 'verbose_name_plural': 'Direcciones_alumnos'},
        ),
        migrations.AlterModelOptions(
            name='pagos',
            options={'ordering': ('fecha_pag', 'alumno'), 'verbose_name': 'Pago', 'verbose_name_plural': 'Pagos'},
        ),
        migrations.AlterModelOptions(
            name='postulacion',
            options={'ordering': ('fecha_post',), 'verbose_name': 'Postulacion', 'verbose_name_plural': 'Postulaciones'},
        ),
        migrations.AlterField(
            model_name='postulacion',
            name='anio_ingreso',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='postulacion',
            name='semestre_ingreso',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
