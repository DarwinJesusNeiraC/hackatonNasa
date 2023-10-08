from django.contrib import admin
from .models import Animal, InfoAnimal, NivelPeligro, Especie, Habitat, Coordenadas

admin.site.register(Animal)
admin.site.register(InfoAnimal)
admin.site.register(NivelPeligro)
admin.site.register(Especie)
admin.site.register(Habitat)
admin.site.register(Coordenadas)
