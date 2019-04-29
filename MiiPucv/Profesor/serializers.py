from Profesor.models import Profesor, Tipo_grado, DireccionProfesor
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Profesor
    fields = '__all__'

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class= ProfesorSerializer

class Tipo_gradoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Tipo_grado
    fields = '__all__'

class Tipo_gradoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_grado.objects.all()
    serializer_class= Tipo_gradoSerializer

class DireccionProfesorSerializer(serializers.ModelSerializer):
  class Meta:
    model = DireccionProfesor
    fields = '__all__'

class DireccionProfesorViewSet(viewsets.ModelViewSet):
    queryset = DireccionProfesor.objects.all()
    serializer_class= DireccionProfesorSerializer