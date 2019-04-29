from itertools import cycle
from django.core.exceptions import ValidationError
import sys
import time


# def digito_verificador(rut):
# 	reversed_digits = map(int, reversed(str(rut)))
# 	factors = cycle(range(2, 8))
# 	s = sum(d * f for d, f in zip(reversed_digits, factors))
# 	print('DIGITO CORRECTO')
# 	return (-s) % 11

 
def digito_verificador(rut):
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
 
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
	if str(res) == dv:
		return 
	elif dv=="K" and res==10:
		return  
	else:
		raise ValidationError('RUT INVALIDO')


 
def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
    """
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False
 
    entrada = raw_input("Ingrese fecha en formato español: ")
