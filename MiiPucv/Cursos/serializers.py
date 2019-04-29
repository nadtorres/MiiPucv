from Cursos.models import Cursos, Lista_alumnos, Detalle_curso, AvanceCurricular
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers

class CursosSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cursos
    fields = '__all__'

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class= CursosSerializer


# -----------API LISTA DE CURSOS-----------
class Lista_alumnosSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Lista_alumnos
    fields = '__all__'

class Lista_alumnosViewSet(viewsets.ModelViewSet):
    queryset = Lista_alumnos.objects.all()
    serializer_class= Lista_alumnosSerializer



# -----------API DETALLE CURSO -----------
class Detalle_cursoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Detalle_curso
    fields = '__all__'

class Detalle_cursoViewSet(viewsets.ModelViewSet):
    queryset = Detalle_curso.objects.all()
    serializer_class= Detalle_cursoSerializer

# -----------API AVANCE CURRICULAR -----------

class Avance_curricularSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = AvanceCurricular
    fields = '__all__'

class Avance_curricularViewSet(viewsets.ModelViewSet):
    queryset = AvanceCurricular.objects.all()
    serializer_class= Avance_curricularSerializer
