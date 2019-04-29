from Sede.models import Sede, DireccionSede
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers

class SedeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Sede
    fields = '__all__'

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class= SedeSerializer

class DireccionSedeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = DireccionSede
    fields = '__all__'

class DireccionSedeViewSet(viewsets.ModelViewSet):
    queryset = DireccionSede.objects.all()
    serializer_class= DireccionSedeSerializer