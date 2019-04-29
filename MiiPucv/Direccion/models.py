from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Region(models.Model):
	id_region = models.AutoField(primary_key=True, null=False)
	nombre = models.CharField(max_length=100, null=False, blank=False)

	class Meta:
		ordering = ('nombre','id_region')
		verbose_name='Region'
		verbose_name_plural='Regiones'


	def __str__(self):
		return self.nombre


	def to_dict_json(self):
		return {
			'id_region': self.id_region,
			'nombre': self.nombre,
		}

class Provincia(models.Model):
	id_provincia = models.AutoField(primary_key=True, null=False)
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, null=False, blank=False)

	class Meta:
		ordering=('region', 'nombre')
		verbose_name='Provincia'
		verbose_name_plural='Provincias'

	def __str__(self):
		return self.nombre


	def to_dict_json(self):
		return {
			'id_provincia': self.id_provincia,
			'region_id': self.region_id,
			'nombre': self.nombre,
		}

class Comuna(models.Model):
	id_comuna = models.AutoField(primary_key=True, null=False)
	provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, null=False, blank=False)

	class Meta:
		ordering=('provincia', 'nombre')
		verbose_name='Comuna'
		verbose_name_plural='Comunas'

	def __str__(self):
		return self.nombre


	def to_dict_json(self):
		return {
			'id_comuna': self.id_comuna,
			'provincia_id': self.provincia_id,
			'nombre': self.nombre,
		}
