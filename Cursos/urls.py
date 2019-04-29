from django.contrib import admin
from django.urls import include, path
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('agregar_curso', views.agregar_curso.as_view(), name='registroCurso'),
	path('malla_curricular', views.cursos_en_malla.as_view(), name='cursos_en_malla'),
	path('cursos/<int:pk>', views.obligatorios_optativos, name='obligatorios_optativos'),
	path('cursos/historicos', views.historicos, name='historicos'),
	path('cursos/historicos/detalle_curso/<int:pk>', views.detalle_curso, name='detalle_curso'),
	path('avance_curricular/<int:pk>', views.avance_curricular, name='avance_curricular'),
	path('cursos/historicos/filtro', views.my_custom_sql, name='my_custom_sql'),

]
