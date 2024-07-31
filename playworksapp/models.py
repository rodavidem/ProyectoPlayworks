from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    consulta = models.CharField(max_length=120)

class Empleo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=20)

class Formulario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    consulta = models.BooleanField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=20)