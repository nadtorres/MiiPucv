# Generated by Django 2.1.3 on 2019-01-18 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Direccion', '__first__'),
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionSede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=300, null=True)),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Comuna')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Provincia')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.AddField(
            model_name='direccionsede',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sede.Sede'),
        ),
    ]
