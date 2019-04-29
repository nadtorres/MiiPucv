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
from Alumno.views import registroAlumno, contacto, sobre_nosotros, alumnosList, direccionList, ficha_academica

from rest_framework import routers, serializers, viewsets, generics
from rest_framework.routers import DefaultRouter

from Alumno.serializers import AlumnoSerializer, AlumnoViewSet, UserSerializer, userViewSet
from Alumno.serializers import BecasSerializer, Cursos_homologadosSerializer, PostulacionSerializer, PagosSerializer, DireccionAlumnoSerializer
from Alumno.serializers import BecasViewSet, Cursos_homologadosViewSet, PostulacionViewSet, PagosViewSet, DireccionAlumnoViewSet
from django.contrib.auth.models import User
from Profesor.serializers import ProfesorSerializer, ProfesorViewSet, Tipo_gradoSerializer, DireccionProfesorSerializer, Tipo_gradoViewSet, DireccionProfesorViewSet
from Cursos.serializers import CursosSerializer, CursosViewSet, Lista_alumnosSerializer, Lista_alumnosViewSet, Detalle_cursoSerializer, Detalle_cursoViewSet, Avance_curricularSerializer, Avance_curricularViewSet
from Direccion.serializers import RegionSerializer, ProvinciaSerializer, ComunaSerializer, RegionViewSet, ProvinciaViewSet, ComunaViewSet
from Documento.serializers import DocumentoViewSet, DocumentoSerializer
from Sede.serializers import SedeViewSet, DireccionSedeViewSet, SedeSerializer, DireccionSedeSerializer

router = routers.DefaultRouter()

# --- RUTA API USUARIOS ------
router.register(r'users', userViewSet)

#---- RUTA API FUNCIONES ALUMNO ----
router.register(r'Alumno', AlumnoViewSet)
router.register(r'Becas', BecasViewSet)
router.register(r'Cursos_homologados', Cursos_homologadosViewSet)
router.register(r'Postulacion', PostulacionViewSet)
router.register(r'Pagos', PagosViewSet)
router.register(r'DireccionAlumno', DireccionAlumnoViewSet)

#---- RUTA API FUNCIONES PROFESOR ------
router.register(r'Profesor', ProfesorViewSet)
router.register(r'Tipo_grado', Tipo_gradoViewSet)
router.register(r'DireccionProfesor', DireccionProfesorViewSet)


# ----- RUTA API DIRECCION -----
router.register(r'Region', RegionViewSet)
router.register(r'Provincia', ProvinciaViewSet)
router.register(r'Comuna', ComunaViewSet)


# ----- RUTA API DOCUMENTO ----
router.register(r'Documento', DocumentoViewSet)


# ---- RUTA API SEDE ------
router.register(r'Sede', SedeViewSet)
router.register(r'DireccionSede', DireccionSedeViewSet)


#---- RUTA API FUNCIONES CURSOS ------
router.register(r'Cursos', CursosViewSet)
router.register(r'Lista_alumnos', Lista_alumnosViewSet)
router.register(r'Detalle_curso', Detalle_cursoViewSet)
router.register(r'Avance_Curricular', Avance_curricularViewSet)



urlpatterns = [
     #-----URL DE FUNCIONALIDADES DE ALUMNOS-----
    path('home', views.index, name="home"),
    path('registroAlumno', views.registroAlumno.as_view(), name='registroAlumno'),
    path('index', views.prueba),
    path('contacto', views.contacto, name='contacto'),
    path('sobreNosotros', views.sobre_nosotros, name='sobreNosotros'),
    path('lista_alumnos', views.alumnosList.as_view(), name='alumnosList'),
    path('datos_direccion_alumno/<int:pk>', views.direccionList.as_view(), name='direccionList'),
    path('editar_direccion/<int:pk>', views.direccionListEditar, name='editar_direccion'),
    path('ficha_academica/<int:pk>', views.ficha_academica, name='ficha_academica'),
    path('agregar_datos_postulacion/<int:pk>', views.postulacionAgregarDatos, name='agregar_datos_postulacion'),
    path('datos_postulacion_alumno/<int:pk>', views.datos_postulacion.as_view(), name='datos_postulacion_alumno'),
    path('editar_postulacion/<int:pk>', views.editar_postulacion, name='editar_postulacion'),
  



    #-----URL DEL LOGIN DE USUARIO --
    path('login/', auth_views.LoginView.as_view(), name='login'),


    #-----URLS PARA CONFIRMACIÓN DE EMAIL EN RECUPERACIÓN DE CONTRASEÑA DE USUARIO---

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]

