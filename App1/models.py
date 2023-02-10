from django.db import models

# Create your models here.

class Estudiantes (models.Model):
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=30)

class Carreras (models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Profesores (models.Model):
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=30)
    

