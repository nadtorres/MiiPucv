from Direccion.models import Region, Provincia, Comuna
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers


class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class= RegionSerializer

class ProvinciaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Provincia
    fields = '__all__'

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class= ProvinciaSerializer

class ComunaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comuna
    fields = '__all__'

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class= ComunaSerializer