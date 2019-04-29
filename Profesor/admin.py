from django.contrib import admin
from Profesor.models import Tipo_grado, Profesor, DireccionProfesor
# Register your models here.

admin.site.register(Tipo_grado)
admin.site.register(Profesor)
admin.site.register(DireccionProfesor)