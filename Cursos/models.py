from django.db import models
from Alumno.models import Alumno
from Profesor.models import Profesor
from datetime import datetime, timedelta
import time
from django.db.models.functions import TruncMonth

# Create your models here.
class Lista_alumnos(models.Model):
	id_lista = models.BigAutoField(null=False, primary_key=True)
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)

	class Meta:
		ordering = ('id_lista', 'alumno')
		verbose_name='Lista'
		verbose_name_plural='Listas'

	def __str__(self):
		return self.id_lista


	def to_dict_json(self):
		return {
			'id': self.id,
			'alumno_id': self.alumno_id,
		}

class Cursos(models.Model):
	nombre = models.CharField(max_length=300, null=False)
	sigla = models.CharField(max_length=10, null=False)
	creditos = models.IntegerField(null=False)
	optativo = 'Optativo'
	obligatorio = 'Obligatorio'
	tipo_curso_choices = (
		(optativo, u'Optativo'),
		(obligatorio, u'Obligatorio'),
	)
	tipo = models.CharField(max_length=12, choices=tipo_curso_choices, blank=False, null=False)
	descripcion = models.CharField(max_length=1000, blank=True, null=True)


	class Meta:
		ordering = ('nombre', 'sigla', 'creditos')
		verbose_name='Curso'
		verbose_name_plural='Cursos'


	def __str__(self):
		cadena = self.nombre+" ("+self.sigla+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'sigla': self.sigla,
			'creditos': self.creditos,
			'tipo': self.get_tipo_display(),
			'descripcion': self.descripcion,
		}


class Detalle_curso(models.Model):
	profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
	lista_alumnos = models.ForeignKey(Lista_alumnos, null=True, blank=True, on_delete=models.CASCADE)
	curso = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
	anio_cursado = models.CharField(max_length=4, null=False, blank=True)
	semestre = models.CharField(max_length=2, null=False, blank=True)
	paralelo = models.IntegerField(null=False)
	aprobados = models.CharField(max_length=300, null=True,blank=True)
	rechazados = models.CharField(max_length=300, null=True, blank=True)
	descripcion = models.CharField(max_length=500, null=True, blank=True)
	inscritos = models.CharField(max_length=500, null=True, blank=True)

	class Meta:
		ordering= ('anio_cursado', 'semestre', 'curso')
		verbose_name='Detalle'
		verbose_name_plural='Detalles'

	def __str__(self):
		cadena = self.anio_cursado
		return cadena

	def to_dict_json(self):
		return {
			'id': self.id,
			'lista_alumnos_id': self.lista_alumnos_id,
			'profesor_id': self.profesor_id,
			'curso_id': self.curso_id,
			'anio_cursado': self.anio_cursado,
			'semestre': self.semestre,
			'paralelo': self.paralelo,
			'aprobados': self.aprobados,
			'rechazados': self.rechazados,
			'descripcion': self.descripcion,
			'inscritos': self.inscritos,
		}


class AvanceCurricular(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	curso = models.ManyToManyField(Cursos, blank=True)
	semestre1 = '1er Semestre'
	semestre2 = '2do Semestre'
	semestre_choices = (
		(semestre1, u'1er Semestre'),
		(semestre2, u'2do Semestre'),
	)
	semestre = models.CharField(max_length=50, choices=semestre_choices, null=True, blank=True)
	anio_cursado = models.CharField(max_length=4, null=False, blank=True)
	en_proceso = 'En proceso'
	aprobado = 'Aprobado'
	rechazado = 'Rechazado'
	retiro = 'Retiro'
	opciones = (
		(en_proceso, u'En proceso'),
		(aprobado, u'Aprobado'),
		(rechazado, u'Rechazado'),
		(retiro, u'Retiro'),
	)
	estado = models.CharField(max_length=300, choices=opciones, blank=False, null=False)
	anio_actual = time.strftime("%Y")


	class Meta:
		ordering= ('anio_cursado', 'estado')
		verbose_name='Avance'
		verbose_name_plural='Avances'

	def __str__(self):
		cadena = self.alumno.nombre+" "+self.alumno.apellido_pat+" "+ self.alumno.apellido_mat
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'estado': self.get_estado_display(),
		}

