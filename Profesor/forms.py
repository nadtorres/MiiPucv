from .models import Profesor, Tipo_grado, DireccionProfesor
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import Select, CheckboxSelectMultiple
from Direccion.models import Region, Provincia, Comuna
from betterforms.multiform import MultiModelForm


class Tipo_gradoForm(forms.ModelForm):
	class Meta:
		model = Tipo_grado
		fields = [
			'nombre_tipo',
			'institucion',
			'nombre',
			'anio_obtencion',
		]
		labels = {
			'nombre_tipo': 'Tipo de Estudio ',
			'institucion': 'Institución ',
			'nombre': 'Nombre ',
			'anio_obtencion': 'Año Obtención',
		}
		widgets = {
			'nombre_tipo': forms.Select(attrs={'class':'form-control'}),
			'institucion': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'anio_obtencion': forms.TextInput(attrs={'class':'form-control'}),
		}

class ProfesorForm(forms.ModelForm):
	class Meta:
		model = Profesor
		fields = [
			'nombre',
			'apellido_pat',
			'apellido_mat',
			'rut',
			'fecha_nac',
			'sexo',
			'telefono',
			'mail',
			'profesion', 
		]
		labels = {
			'nombre': 'Nombres ',
			'apellido_pat': 'Apellido Paterno ',
			'apellido_mat': 'Apellido Materno ',
			'rut': 'RUT',
			'fecha_nac': 'Fecha Nacimiento ',
			'sexo': 'Seleccione sexo ',
			'telefono': 'Teléfono ',
			'mail': 'Email ',
			'profesion': 'Título Profesional ', 	
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido_pat': forms.TextInput(attrs={'class':'form-control'}),
			'apellido_mat': forms.TextInput(attrs={'class':'form-control'}),
			'rut': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nac': forms.SelectDateWidget(attrs={'class':'form-control'}),
			'sexo': forms.Select(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'mail': forms.EmailInput(attrs={'class': 'form-control'}),
			'profesion': forms.TextInput(attrs={'class':'form-control'}),
		}

class DireccionProfesorForm(forms.ModelForm):
	class Meta:
		model = DireccionProfesor
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


class ProfesorGradoForm(MultiModelForm):
    form_classes = {
        'profesor': ProfesorForm,
        'tipogrado': Tipo_gradoForm,
        'direccion': DireccionProfesorForm,
    }
    def save(self, commit=True):
        objects = super(ProfesorGradoForm, self).save(commit=False)

        if commit:
            profesor = objects['profesor']
            profesor.save()
            tipogrado = objects['tipogrado']
            tipogrado.profesor = profesor
            tipogrado.save()
            direccion = objects['direccion']
            direccion.profesor = profesor
            direccion.save()
            return objects