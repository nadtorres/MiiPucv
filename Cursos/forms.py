from Cursos.models import Detalle_curso, Lista_alumnos, Cursos, AvanceCurricular
from django import forms

class Detalle_curso_form(forms.ModelForm):
	class Meta:
		model = Detalle_curso
		fields = [
			'profesor',
			'lista_alumnos',
			'curso',
			'anio_cursado',
			'semestre',
			'paralelo',
			'aprobados',
			'rechazados',
			'descripcion', 
		]
		labels = {
			'profesor': 'Profesor encargado:',
			'lista_alumnos': 'Lista de alumnos:',
			'curso': 'Curso:',
			'anio_cursado': 'Año en que fue cursado:',
			'semestre': 'Semestre en que fue cursado:',
			'paralelo': 'Paralelo:', 
			'aprobados': 'Aprobados:',
			'rechazados': 'Rechazados',
			'descripcion': 'Descripción:', 
		}
		widgets = {
			'anio_cursado': forms.SelectDateWidget(attrs={'class':'form-control'}),
			'semestre': forms.NumberInput(attrs={'class':'form-control'}),
			'paralelo': forms.NumberInput(attrs={'class':'form-control'}),
			'aprobados': forms.NumberInput(attrs={'class': 'form-control'}), 
			'rechazados': forms.NumberInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}), 		
		}

class Lista_alumnos_form(forms.ModelForm):
	class Meta:
		model = Lista_alumnos
		fields = [
			'id_lista',
		]
		labels = {
			'id_lista': 'Identificador de Lista:'
		}
		widgets = {
			'id_lista': forms.NumberInput(attrs={'class':'form-control'}),
		}

class Cursos_form(forms.ModelForm):
	class Meta:
		model = Cursos
		fields = [
			'nombre',
			'sigla',
			'creditos',
			'tipo',
			'descripcion',
		]
		labels = {
			'nombre': 'Nombre ',
			'sigla': 'Clave ',
			'creditos': 'Créditos ',
			'tipo': 'Seleccione tipo de curso ',
			'descripcion': 'Ingrese una descripción del curso',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sigla': forms.TextInput(attrs={'class':'form-control'}),
			'creditos': forms.NumberInput(attrs={'class':'form-control'}),
			'tipo': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'})
		}

class Avance_form(forms.ModelForm):
	class Meta:
		model = AvanceCurricular
		fields = [
			'estado',
		]
		labels = {
			'estado': 'Estado'
		}