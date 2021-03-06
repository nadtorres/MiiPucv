# Generated by Django 2.1.3 on 2019-01-18 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Direccion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido_pat', models.CharField(max_length=30)),
                ('apellido_mat', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=12, null=True)),
                ('fecha_nac', models.DateField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=20, null=True)),
                ('mail', models.EmailField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id_beca', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('monto', models.CharField(max_length=9)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos_homologados',
            fields=[
                ('id_curso', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='DireccionAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=300, null=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Comuna')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Provincia')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Direccion.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_pag', models.DateField()),
                ('monto', models.IntegerField()),
                ('tipo_pago', models.CharField(choices=[('Transferencia', 'Transferencia'), ('Efectivo', 'Efectivo'), ('Cheque', 'Cheque'), ('Credito', 'Credito'), ('Debito', 'Debito')], max_length=30)),
                ('banco', models.CharField(max_length=50, null=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_post', models.DateField()),
                ('universidad_procedencia', models.CharField(max_length=100)),
                ('carrera_procedencia', models.CharField(max_length=100)),
                ('nivelacion', models.CharField(choices=[('Necesita', 'Necesita'), ('No necesita', 'No necesita')], max_length=30)),
                ('semestre_ingreso', models.IntegerField(null=True)),
                ('anio_ingreso', models.IntegerField(null=True)),
                ('estado_matricula', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20, null=True)),
                ('antecedentes_academicos', models.IntegerField(null=True)),
                ('antecedentes_profesionales', models.IntegerField(null=True)),
                ('carta_recomendacion', models.IntegerField(null=True)),
                ('entrevista', models.CharField(max_length=30, null=True)),
                ('puntaje', models.IntegerField(null=True)),
                ('resultados_condicion', models.CharField(choices=[('Aprueba', 'Aprueba'), ('Reprueba', 'Reprueba')], max_length=30)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='becas',
            field=models.ManyToManyField(blank=True, to='Alumno.Becas'),
        ),
    ]
