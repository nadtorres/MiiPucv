from django.db import models

# Create your models here.

class Pagos(models.Model):
	id_pago = models.IntegerField(null=False, primary_key=True)
	fecha_pag = models.DateField(null=False)
	monto = models.IntegerField(null=False)
	transferencia = 'Transferencia'
	efectivo = 'Efectivo'
	cheque = 'Cheque'
	credito = 'Credito'
	debito = 'Debito'
	tipo_pago_choices = (
		(transferencia, u'Transferencia'),
		(efectivo, u'Efectivo'),
		(cheque, u'Cheque'),
		(credito, u'Credito'),
		(debito, u'Debito'),
	)
	tipo_pago = models.CharField(max_length=30, choices=tipo_pago_choices, blank=False, null=False)
	banco = models.CharField(max_length=50, null=True)
