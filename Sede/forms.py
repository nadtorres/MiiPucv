from Sede.models import Sede, DireccionSede
from django import forms

class Sede_form(forms.ModelForm):
	model = Sede
	fields = [
		'nombre',
	]
	labels = {
		'nombre': 'Nombre: ',
	}

class DireccionForm(forms.ModelForm):
	class Meta:
		model = DireccionSede
		fields = [
			'region',
			'provincia',
			'comuna',
			'direccion',
		]
		labels = {
			'region': 'Región',
			'provincia': 'Provincia',
			'comuna': 'Comuna',
			'direccion': 'Dirección',
		}
		widgets = {
			'region': forms.Select(attrs={'class':'form-control'}),
			'provincia': forms.Select(attrs={'class':'form-control'}),
			'comuna': forms.Select(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
		}

