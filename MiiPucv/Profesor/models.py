from django.db import models
from Direccion.models import Region, Provincia, Comuna
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
# Create your models here.

class Profesor(models.Model):
	nombre = models.CharField(max_length=100, null=False)
	apellido_pat = models.CharField(max_length=50, null=False)
	apellido_mat = models.CharField(max_length=50, null=False)
	rut = models.CharField(max_length=13)
	fecha_nac = models.DateField(null=False)
	sexo_masculino = 'Masculino'
	sexo_femenino = 'Femenino'
	sexo_otro = 'Otro'
	sexo_choices = (
		(sexo_masculino, u'Masculino'),
		(sexo_femenino, u'Femenino'),
		(sexo_otro, u'Otro'),
	)
	sexo = models.CharField(max_length=20, choices=sexo_choices, blank=True)
	telefono = models.CharField(max_length=12, null=True)
	mail = models.EmailField(max_length=300, blank=True, null=True)
	profesion = models.CharField(max_length=50)

	class Meta:
		ordering=('nombre', 'apellido_pat')
		verbose_name='Profesor'
		verbose_name_plural='Profesores'

	def __str__(self):
		cadena = self.nombre+" "+self.apellido_pat+" "+self.apellido_mat+" ("+self.rut+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido_pat': self.apellido_pat,
			'apellido_mat': self.apellido_mat,
			'rut': self.rut,
			'fecha_nac': self.fecha_nac,
			'sexo': self.get_sexo_display(),
			'telefono': self.telefono,
			'mail': self.mail,
			'profesion': self.profesion,
		}

class Tipo_grado(models.Model):
	profesor = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
	licenciatura = 'Licenciatura'
	titulo_profesional = 'Titulo Profesional'
	magister = 'Magister'
	doctorado = 'Doctorado'
	nombre_tipo_choices = (
		(licenciatura, u'Licenciatura'),
		(titulo_profesional, u'Titulo Profesional'),
		(magister, u'Magister'),
		(doctorado, u'Doctorado'),
	)
	nombre_tipo = models.CharField(max_length=30, choices=nombre_tipo_choices, blank=False, null=False)
	institucion = models.CharField(max_length=100, null=True)
	nombre = models.CharField(max_length=200, null=True)
	anio_obtencion = models.CharField(max_length=4, null=True)

	class Meta:
		ordering=('profesor','nombre_tipo')
		verbose_name='Grado'
		verbose_name_plural='Grados'

	def __str__(self):
		cadena = self.nombre_tipo+" ("+self.institucion+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'profesor_id': self.profesor_id,
			'nombre_tipo': self.get_nombre_tipo_display(),
			'institucion': self.institucion,
			'nombre': self.nombre,
			'anio_obtencion': self.anio_obtencion,
		}

class DireccionProfesor(models.Model):
	profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
	provincia = GroupedForeignKey(Provincia, 'region')
	comuna = GroupedForeignKey(Comuna, 'provincia')
	direccion = models.CharField(max_length=300, null=True)

	class Meta:
		ordering=('region', 'provincia', 'comuna')
		verbose_name='Direccion'
		verbose_name_plural='Direcciones'


	def __str__(self):
		cadena = self.region.nombre+", "+self.direccion+"("+self.profesor.nombre+" "+self.profesor.apellido_pat+" "+self.profesor.apellido_mat+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'profesor_id': self.profesor_id,
			'region_id': self.region_id,
			'provincia_id': self.provincia_id,
			'comuna_id': self.comuna_id,
			'direccion': self.direccion,
		}