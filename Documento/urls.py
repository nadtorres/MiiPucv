from django.contrib import admin
from django.urls import include, path



path('acta_interna', views.acta_interna, name ="acta_interna"),
path('certificado_Egreso', views.certificado_Egreso, name="certificado_Egreso"),
path('actaExamenGrado', views.actaExamenGrado, name="actaExamenGrado"),
path('crear_expediente', views.crear_expediente, name="crear_expediente"),