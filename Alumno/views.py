from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from .forms import Cursos_homologadosForm, DireccionForm, AlumnoForm, PostulacionForm, PagosForm, BecasForm
from .models import Alumno, Becas, Cursos_homologados, Postulacion, Pagos, DireccionAlumno
from django.urls import reverse_lazy
from Direccion.models import Region, Provincia, Comuna
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required()
def index(request):
    return render(request, 'Base/home.html')

@login_required()
def prueba(request):
    return render(request, 'Alumno/index.html')

@login_required
def sobre_nosotros(request):
    return render(request, 'Contacto/sobre_nosotros.html')

@login_required
def contacto(request):
    return render(request, 'Contacto/contacto.html')

class registroAlumno(LoginRequiredMixin, CreateView):
    model = DireccionAlumno
    template_name = 'Alumno/registro_alumno.html'
    form_class = DireccionForm
    second_form_class = AlumnoForm
    success_url = reverse_lazy('registroAlumno')

    def get_context_data(self, **kwargs):
        context = super(registroAlumno, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)        
        if form.is_valid() and form2.is_valid():
            direccion = form.save(commit=False)
            direccion.alumno = form2.save()   
            direccion.save()
            messages.success(request, 'Se ha agregado correctamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.warning(request,'Rut Invalido, ingrese datos nuevamente')
            return HttpResponseRedirect(self.get_success_url())

class alumnosList(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'Alumno/alumnosList.html'
    form_class = AlumnoForm
    second_form_class = DireccionForm
    third_form_class = PostulacionForm
    paginate_by = 10

class direccionList(LoginRequiredMixin, UpdateView):
    model = DireccionAlumno
    template_name = 'Alumno/datos_direccion.html'
    form_class = DireccionForm
    success_url = reverse_lazy('lista_alumnos')

@login_required()
def direccionListEditar(request, pk):
    direccion = DireccionAlumno.objects.get(pk=pk)
    if request.method == 'GET':
        form = DireccionForm(instance=direccion)
    else:
        form = DireccionForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado la información correctamente')
        return redirect('direccionList', pk)
    return render(request, 'Alumno/editar_direccion.html', {'form':form})


@login_required()
def ficha_academica(request, pk):

    objeto1 = Alumno.objects.filter(id=pk)
    objeto2 = DireccionAlumno.objects.filter(alumno_id=pk)
    objeto3 = Postulacion.objects.filter(alumno_id=pk)

    return render(request, 'Alumno/ficha_academica.html', {'alumno': objeto1, 'direccion': objeto2, 'postulacion': objeto3})


@login_required()
def postulacionAgregarDatos(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    postulacion = PostulacionForm(request.POST or None)
    if postulacion.is_valid():
        agregar_postulacion = postulacion.save(commit=False) #todavía no lo guardo
        agregar_postulacion.alumno = alumno #le agrego el id del alumno
        agregar_postulacion.save() #lo guardo
        messages.success(request, 'Se ha agregado correctamente')
        return redirect('ficha_academica', pk)

    return render(request, 'Alumno/agregar_datos_postulacion.html', {'form': postulacion})


class datos_postulacion(LoginRequiredMixin, UpdateView):
    model = Postulacion
    template_name = 'Alumno/datos_postulacion.html'
    form_class = PostulacionForm
    success_url = reverse_lazy('datos_postulacion_alumno')

@login_required()
def editar_postulacion(request, pk): 
    postulacion = get_object_or_404(Postulacion, alumno_id=pk)
    form = PostulacionForm(request.POST or None, instance=postulacion)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se ha editado la información correctamente')
        return redirect('datos_postulacion_alumno', pk)
    return render(request, 'Alumno/editar_postulacion.html', {'form': form}) 











#class ficha_academica(LoginRequiredMixin, DetailView):
 #   model = Alumno
  #  second_model = DireccionAlumno
   # fields = '__all__'
   # template_name = 'Alumno/ficha_academica.html'
   # form_class = AlumnoForm
   # second_form_class = DireccionForm
   # success_url = reverse_lazy('datos_direccion')
#
 #   def get_context_data(self, **kwargs):
  #      context = super(ficha_academica, self).get_context_data(**kwargs)
   #     pk = self.kwargs.get('pk', 0)
    #    alumno = self.model.objects.get(id=pk)
     #   direccion = self.second_model.objects.get(id=pk)
      #  context['id'] = pk
       # return context 
