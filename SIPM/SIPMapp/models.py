from django.db import models

# Create your models here.

class Algo(models.Model):
 
    nombre_algo = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)



