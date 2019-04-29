from django.db import models
from Alumno.models import Alumno
from Profesor.models import Profesor

# Create your models here.

class Documento(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, null=False)
	tesis = 'Tesis'
	investigacion = 'Investigacion'
	tipo_choices = (
		(tesis, u'Tesis'),
		(investigacion, u'Investigacion'),
	)
	tipo_doc = models.CharField(max_length=20, choices=tipo_choices, null=False)

	class Meta:
		ordering=('tipo_doc','nombre', 'alumno', 'profesor')
		verbose_name='Documento'
		verbose_name_plural='Documentos'


	def __str__(self):
		cadena = self.nombre+" ("+self.tipo_doc+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'alumno_id': self.alumno_id,
			'profesor_id': self.profesor_id,
			'nombre': self.nombre,
			'tipo_doc': self.get_tipo_doc_display(),
		}