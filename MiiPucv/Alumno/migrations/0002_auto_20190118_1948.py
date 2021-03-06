# Generated by Django 2.1.3 on 2019-01-18 19:48

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionalumno',
            name='comuna',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='provincia', on_delete=django.db.models.deletion.CASCADE, to='Direccion.Comuna'),
        ),
        migrations.AlterField(
            model_name='direccionalumno',
            name='provincia',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='region', on_delete=django.db.models.deletion.CASCADE, to='Direccion.Provincia'),
        ),
    ]
