from Alumno.models import Cursos_homologados, Alumno, Postulacion, Pagos, Becas, DireccionAlumno
from django import forms
from django.forms.widgets import Select, SelectMultiple, Media
from Direccion.models import Region, Provincia, Comuna
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.forms import ChoiceField
from smart_selects.widgets import ChainedSelect, ChainedSelectMultiple
from django.utils.encoding import force_text
from betterforms.multiform import MultiModelForm


class Cursos_homologadosForm(forms.ModelForm):
	class Meta:
		model = Cursos_homologados
		fields = [
			'id_curso',
			'nombre',
		]
		labels = {
			'id_curso': 'Número de Curso:',
			'nombre': 'Nombre:',
		}

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = [
			'nombre', 
			'apellido_pat',
			'apellido_mat',
			'rut', 
			'telefono',
			'fecha_nac', 
			'sexo',
			'mail',
		]
		labels = {
			'nombre': 'Nombres: ', 
			'apellido_pat': 'Apellido Paterno:',
			'apellido_mat': 'Apellido Materno:',
			'rut': 'RUT:', 
			'telefono': 'Teléfono:',
			'fecha_nac': 'Fecha de Nacimiento:', 
			'sexo': 'Seleccione Sexo:',
			'mail': 'Email: ',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido_pat': forms.TextInput(attrs={'class':'form-control'}),
			'apellido_mat': forms.TextInput(attrs={'class':'form-control'}),
			'rut': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nac': forms.DateInput(attrs={'class':'form-control'}),
			'sexo': forms.Select(attrs={'class':'form-control'}),
			'mail': forms.EmailInput(attrs={'class': 'form-control'}),
			'beca': forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
		}

class PostulacionForm(forms.ModelForm):
	class Meta:
		model = Postulacion
		fields = [
			'fecha_post',
			'universidad_procedencia',
			'carrera_procedencia',
			'nivelacion',
			'semestre_ingreso',
			'anio_ingreso',
			'estado_matricula',
			'antecedentes_academicos',
			'antecedentes_profesionales',
			'carta_recomendacion',
			'entrevista',
			'puntaje',
			'resultados_condicion',
		]
		labels = {
			'fecha_post': 'Fecha de Postulación (ej. 01/01/2019) ',
			'universidad_procedencia': 'Universidad de Procedencia ',
			'carrera_procedencia': 'Carrera de Procedencia ',
			'nivelacion': 'Seleccione Estado de Nivelación ',
			'semestre_ingreso': 'Semestre de Ingreso ',
			'anio_ingreso': 'Año de Ingreso (ej. 01/01/2019)',
			'estado_matricula': 'Seleccione Estado de Matrícula ',
			'antecedentes_academicos': 'Ingrese Antecedentes Académicos',
			'antecedentes_profesionales': 'Ingrese Antecedentes Profesionales ',
			'carta_recomendacion': 'Ingrese Puntaje de Carta de Recomendación ',
			'entrevista': 'Ingrese Puntaje de Entrevista',
			'puntaje': 'Ingrese Puntaje Final ',
			'resultados_condicion': 'Seleccione el Estado Final del Alumno',	
		}
		widgets = {
			'fecha_post': forms.DateInput(attrs={'class': 'form-control'}),
			'universidad_procedencia': forms.TextInput(attrs={'class': 'form-control'}),
			'carrera_procedencia': forms.TextInput(attrs={'class':'form-control'}),
			'nivelacion': forms.Select(attrs={'class':'form-control'}),
			'semestre_ingreso': forms.NumberInput(attrs={'class':'form-control'}),
			'anio_ingreso' : forms.NumberInput(attrs={'class':'form-control'}),
			'estado_matricula': forms.Select(attrs={'class':'form-control'}),
			'antecedentes_academicos': forms.NumberInput(attrs={'class':'form-control'}),
			'antecedentes_profesionales': forms.NumberInput(attrs={'class':'form-control'}),
			'carta_recomendacion':forms.NumberInput(attrs={'class':'form-control'}),
			'entrevista': forms.TextInput(attrs={'class':'form-control'}),
			'puntaje': forms.NumberInput(attrs={'class':'form-control'}),
			'resultados_condicion': forms.Select(attrs={'class':'form-control'}),
		}

class PagosForm(forms.ModelForm):
	class Meta:
		model = Pagos
		fields = [
			'id_pago',
			'fecha_pag',
			'monto',
			'tipo_pago',
			'banco',
		]
		labels = {
			'id_pago': 'Número de pago: ',
			'fecha_pag': 'Fecha de Pago: ',
			'monto': 'Monto: ',
			'tipo_pago': 'Seleccione tipo de pago: ',
			'banco': 'Ingrese Banco: ',
		}


class BecasForm(forms.ModelForm):
	class Meta:
		model = Becas
		fields = [
			'id_beca',
			'nombre',
			'monto',
			'tipo',
		]
		labels = {
			'id_beca': 'Número de Beca:',
			'nombre': 'Nombre: ',
			'monto': 'Ingrese Monto de Beca:',
			'tipo': 'Seleccione el tipo de Beca:',			
		}

class DireccionForm(forms.ModelForm):
	class Meta:
		model = DireccionAlumno
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


