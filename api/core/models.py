from django.db import models


# Create your models here.


#class Campo(models.Model):
    
class Campo(models.Model):
    n = models.CharField(max_length=250)
    campo = models.CharField(max_length=250)
    desc = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    tamnh = models.CharField(max_length=250)
    dec = models.CharField(max_length=250)
    obrg = models.CharField(max_length=250)



