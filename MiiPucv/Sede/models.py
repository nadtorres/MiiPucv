from django.db import models
from Alumno.models import Alumno
from Direccion.models import Region, Provincia, Comuna
# Create your models here.

class Sede(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50, null=False)

	class Meta:
		ordering=('nombre', 'alumno')
		verbose_name='Sede'
		verbose_name_plural='Sedes'


	def __str__(self):
		return self.nombre


	def to_dict_json(self):
		return {
			'id': self.id,
			'alumno_id': self.id,
			'nombre': self.nombre
		}


class DireccionSede(models.Model):
	sede = models.ForeignKey(Sede, null=True, blank=True, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
	provincia = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)
	comuna = models.ForeignKey(Comuna, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=300, null=True)

	class Meta:
		ordering=('region', 'provincia', 'comuna', 'sede')
		verbose_name='DireccionSede'
		verbose_name_plural='DireccionesSede'


	def __str__(self):
		cadena = self.region.nombre+", "+self.provincia.nombre+" "+self.comuna.nombre+"("+self.direccion+")"
		return cadena

	def to_dict_json(self):
		return {
			'id': self.id,
			'sede_id': self.sede_id,
			'region_id': self.region_id,
			'provincia_id': self.provincia_id,
			'comuna_id': self.comuna_id,
			'direccion': self.direccion,
		}