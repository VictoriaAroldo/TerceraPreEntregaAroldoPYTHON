from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)       
    contrasenia = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    mail = models.EmailField()
    tel = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)