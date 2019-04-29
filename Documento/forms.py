from Documento.models import Documento
from django import forms

class Documento_form(forms.ModelForm):
	model = Documento
	fields = [
		'id_doc',
		'nombre', 
		'tipo_doc',
	]
	labels = {
		'id_doc': 'Número de Documento: ',
		'nombre': 'Nombre Documento: ', 
		'tipo_doc': 'Seleccione tipo de Documento: ',
	}