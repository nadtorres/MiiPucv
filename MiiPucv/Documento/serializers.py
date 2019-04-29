from Documento.models import Documento
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import routers

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Documento
    fields = '__all__'

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class= DocumentoSerializer