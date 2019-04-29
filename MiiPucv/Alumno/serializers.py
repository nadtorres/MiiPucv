from Alumno.models import Alumno, Becas, Cursos_homologados, Postulacion, Pagos, DireccionAlumno
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers
from django.contrib.auth.models import User
from Cursos.models import AvanceCurricular



class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Alumno
    fields = '__all__'

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class= AlumnoSerializer

class BecasSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Becas
    fields = '__all__'

class BecasViewSet(viewsets.ModelViewSet):
    queryset = Becas.objects.all()
    serializer_class= BecasSerializer

class Cursos_homologadosSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cursos_homologados
    fields = '__all__'

class Cursos_homologadosViewSet(viewsets.ModelViewSet):
    queryset = Cursos_homologados.objects.all()
    serializer_class= Cursos_homologadosSerializer

class PostulacionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Postulacion
    fields = '__all__'

class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all()
    serializer_class= PostulacionSerializer

class PagosSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pagos
    fields = '__all__'

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class= PagosSerializer

class DireccionAlumnoSerializer(serializers.ModelSerializer):
  class Meta:
    model = DireccionAlumno
    fields = '__all__'

class DireccionAlumnoViewSet(viewsets.ModelViewSet):
    queryset = DireccionAlumno.objects.all()
    serializer_class= DireccionAlumnoSerializer



# ------------SERIALIZERS DE USUARIOS ------------


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer

