# Generated by Django 2.1.3 on 2019-03-11 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ('tipo_doc', 'nombre', 'alumno', 'profesor'), 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
    ]
