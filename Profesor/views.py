from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .forms import ProfesorForm, Tipo_gradoForm, DireccionProfesorForm, ProfesorGradoForm
from .models import Profesor, Tipo_grado, DireccionProfesor
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.

def tipoGrado(request):
    return render(request, 'Profesor/tipo_grado.html', {})

class registroProfesor(LoginRequiredMixin, CreateView):
    form_class = ProfesorGradoForm
    template_name = 'Profesor/registro_profesor.html'
    success_url = reverse_lazy('registroProfesor')

class profesorList(LoginRequiredMixin, ListView):
	model = Profesor
	template_name = 'Profesor/profesorList.html'
	form_class = ProfesorForm
	success_url = reverse_lazy('profesorList')
	paginate_by = 10

@login_required()
def ficha_docente(request, pk):
	objeto1 = Profesor.objects.filter(id=pk)
	objeto2 = DireccionProfesor.objects.filter(profesor_id=pk)
	objeto3 = Tipo_grado.objects.filter(profesor_id=pk)

	return render(request, 'Profesor/ficha_docente.html', {'profesor': objeto1, 'direccion': objeto2, 'grado': objeto3})


@login_required()
def agregar_grado(request, pk):
	profesor = get_object_or_404(Profesor, pk=pk)
	grado = Tipo_gradoForm(request.POST or None)
	if grado.is_valid():
		nuevo_grado = grado.save(commit=False) #todavía no lo guardo
		nuevo_grado.profesor = profesor #le agrego el id del profesor
		nuevo_grado.save() #lo guardo
		messages.success(request, 'Se ha agregado correctamente')
		return redirect('ficha_docente', pk)

	return render(request, 'Profesor/agregar_grado.html', {'form': grado})


class direccionListProfesor(LoginRequiredMixin, UpdateView):
    model = DireccionProfesor
    template_name = 'Profesor/datos_direccion.html'
    form_class = DireccionProfesorForm
    success_url = reverse_lazy('lista_profesores')

@login_required()
def direccionListEditarProfesor(request, pk):
    direccion = DireccionProfesor.objects.get(profesor_id=pk)
    if request.method == 'GET':
        form = DireccionProfesorForm(instance=direccion)
    else:
        form = DireccionProfesorForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado la información correctamente')
        return redirect('datos_direccion', pk)
    return render(request, 'Profesor/editar_direccion.html', {'form':form})