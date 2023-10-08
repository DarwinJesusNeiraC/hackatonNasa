from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

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
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    #infoAnimal = models.OneToOneField(InfoAnimal, on_delete=models.CASCADE)
    descripcion = models.TextField()

class MultimediaAnimal(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    videos = models.TextField()
    modeloAr = models.CharField(max_length=200)
    icono = models.ImageField(upload_to='iconos/', null=True, blank=True)
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)

class Coordenadas(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    #infoAnimal = models.ForeignKey(InfoAnimal, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()
