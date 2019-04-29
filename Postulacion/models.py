from django.db import models

# Create your models here.

class Postulacion(models.Model):
	id_postulacion = models.IntegerField(null=False, primary_key=True)
	fecha_post = models.DateField(null=False)
	universidad_procedencia = models.CharField(max_length=100, null=False)
	carrera_procedencia = models.CharField(max_length=100, null=False)
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
	)
	nivelacion = models.CharField(max_length=30, choices=nivelacion_choices, blank=False, null=False)
	semestre_ingreso = models.IntegerField(null=True)	
	anio_ingreso = models.IntegerField(null=True)
	estado_activo = 'Activo'
	estado_inactivo = 'Inactivo'
	estado_choices = (
		(estado_activo, u'Activo'),
		(estado_inactivo, u'Inactivo'),
	)
	estado_matricula = models.CharField(max_length=20, choices=estado_choices, blank=False, null=True)
	antecedentes_academicos = models.IntegerField(null=True)
	antecedentes_profesionales = models.IntegerField(null=True)
	carta_recomendacion = models.IntegerField(null=True)
	entrevista = models.CharField(max_length=30, null=True)
	puntaje = models.IntegerField(null=True)
	aprueba_condicion = 'Aprueba'
	reprueba_condicion = 'Reprueba'
	resultadoCondicion_choices = (
		(aprueba_condicion, u'Aprueba'),
		(reprueba_condicion, u'Reprueba')
	)
	resultados_condicion = models.CharField(max_length=30, choices=resultadoCondicion_choices, blank=False)