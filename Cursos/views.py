from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from .forms import Detalle_curso_form, Lista_alumnos_form, Cursos_form, Avance_form
from .models import Lista_alumnos, Detalle_curso, Cursos, AvanceCurricular
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from Profesor.models import Profesor
from django.contrib.messages.views import SuccessMessageMixin

# --------- API REST -------------
from Cursos.models import AvanceCurricular
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class agregar_curso(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Cursos
	template_name = 'Cursos/agregar_curso.html'
	form_class = Cursos_form
	success_url = reverse_lazy('registroCurso')
	success_message = "El curso fue creado satisfactoriamente"

class cursos_en_malla(LoginRequiredMixin, ListView):
	model = Cursos
	template_name = 'Cursos/cursos_en_malla.html'
	form_class = Cursos_form
	success_url = reverse_lazy('cursos_en_malla')

@login_required()
def obligatorios_optativos(request, pk):
	model = Cursos
	cursos = Cursos.objects.get(id=pk)
	if cursos.tipo == 'Obligatorio':
		return render(request, 'Cursos/cursos_obligatorios.html', {'cursos': cursos})
	else:
		return render(request, 'Cursos/cursos_optativos.html', {'cursos': cursos})
	return render (request, 'Cursos/cursos_en_malla.html')


# CLASE QUE MUESTRA CURSOS HISTORICOS EN PLANTILLA DE BUSQUEDA
#class historicos(LoginRequiredMixin, ListView):
	#model = Detalle_curso
	#template_name = 'Cursos/historicos.html'
	#form_class = Detalle_curso_form
	#success_url = reverse_lazy('historicos')


# FUNCIÓN QUE MUESTRA LOS CURSOS EN PLANTILLA DE BÚSQUEDA
@login_required()
def historicos(request):
	context = {}
	lista_detalle = Detalle_curso.objects.all()
	context['lista_detalle']= lista_detalle
	return render (request, 'Cursos/historicos.html', context)


@login_required()
def detalle_curso(request, pk):
	curso = Detalle_curso.objects.get(curso_id=pk)
	return render(request, 'Cursos/detalle_curso.html', {'curso': curso})

@login_required()
def avance_curricular(request, pk):
	avance = AvanceCurricular.objects.filter(alumno_id=pk) #se usa filter por coincidencias del M2M, replicará x veces encontrado el resultado
	return render(request, 'Alumno/avance_curricular.html', {'avance': avance})

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute('SELECT anio_cursado FROM "Cursos_detalle_curso"', [self.baz])
        row = cursor.fetchone()

    return row