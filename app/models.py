from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    cargo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    sueldo_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def calcular_descuento(self):
        sueldo_base = self.sueldo_total
        
        if sueldo_base > 3600:
            porcentaje_descuento = 10
        elif sueldo_base > 1800:
            porcentaje_descuento = 5
        else:
            porcentaje_descuento = 0
        
        descuento = sueldo_base * (Decimal(porcentaje_descuento) / 100)
        return descuento


    def calcular_sueldo_neto(self):
        descuento = self.calcular_descuento
        sueldo_neto = self.sueldo_total - descuento
        return sueldo_neto