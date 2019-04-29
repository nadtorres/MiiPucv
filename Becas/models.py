from django.db import models

# Create your models here.

class Becas(models.Model):
	id_beca = models.IntegerField(null=False, primary_key=True)
	nombre = models.CharField(max_length=100, null=False)
	monto = models.CharField(max_length=9, null=False)
	tipo = models.CharField(max_length=100, null=False)
