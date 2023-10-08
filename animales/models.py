from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    #def __str__(self):
    #   return self.nombre

class InfoAnimal(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    nombreCientifico = models.CharField(max_length=100)
    descripcion = models.TextField()
    ultimaModificacion = models.DateTimeField(auto_now=True)
    calificacion = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

class NivelPeligro(models.Model):
    infoAnimal = models.OneToOneField(InfoAnimal, on_delete=models.CASCADE)
    descripcion = models.TextField()
    color = models.CharField(max_length=100)

class Especie(models.Model):
    infoAnimal = models.OneToOneField(InfoAnimal, on_delete=models.CASCADE)
    descripcion = models.TextField()

class Habitat(models.Model):
    infoAnimal = models.OneToOneField(InfoAnimal, on_delete=models.CASCADE)
    descripcion = models.TextField()

class Coordenadas(models.Model):
    infoAnimal = models.ForeignKey(InfoAnimal, on_delete=models.CASCADE)
    coordenada = models.CharField(max_length=100)
