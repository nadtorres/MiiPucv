from django.contrib import admin
from Alumno.models import Alumno, Postulacion, Cursos_homologados, Pagos, Becas, DireccionAlumno

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Postulacion)
admin.site.register(Pagos)
admin.site.register(Becas)
admin.site.register(DireccionAlumno)