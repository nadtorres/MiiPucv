from django.contrib import admin
from Cursos.models import Cursos, Detalle_curso, AvanceCurricular
# Register your models here.

admin.site.register(Cursos)
class EnvioModuloAdmin (admin.ModelAdmin):
    list_display=('anio_cursado')
    # list_filter = ['anio_cursado']
    # date_hierarchy = 'anio_cursado'
    
admin.site.register(Detalle_curso)
admin.site.register(AvanceCurricular)

