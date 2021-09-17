from django.db import models

class Transaccion(models.Model):
    cuenta = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=50)
    movimiento = models.CharField(max_length=100,blank=True)
    nivel = models.CharField(max_length=100,blank=True)
    moneda = models.CharField(max_length=100,blank=True)
    asiento = models.CharField(max_length=100,blank=True)
    ctacargo = models.CharField(max_length=100,blank=True)
    ctaabono = models.CharField(max_length=100,blank=True)
    codant = models.CharField(max_length=100,blank=True)
    oficina = models.CharField(max_length=100,blank=True)
    banco = models.CharField(max_length=100,blank=True)
    proyecto = models.CharField(max_length=100,blank=True)

    def __str__(self):
        template = '{0.cuenta} {0.nombre} {0.movimiento} {0.oficina}'
        return template.format(self)  

class Cincuenta(models.Model):
    cuenta = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=50)
    movimiento = models.CharField(max_length=100,blank=True)
    nivel = models.CharField(max_length=100,blank=True)
    moneda = models.CharField(max_length=100,blank=True)
    asiento = models.CharField(max_length=100,blank=True)
    ctacargo = models.CharField(max_length=100,blank=True)
    ctaabono = models.CharField(max_length=100,blank=True)
    codant = models.CharField(max_length=100,blank=True)
    oficina = models.CharField(max_length=100,blank=True)
    banco = models.CharField(max_length=100,blank=True)
    proyecto = models.CharField(max_length=100,blank=True)

    def __str__(self):
        template = '{0.cuenta} {0.nombre} {0.movimiento} {0.oficina}'
        return template.format(self)  
