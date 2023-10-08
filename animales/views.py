from django.shortcuts import render
from .models import Animal, InfoAnimal, NivelPeligro, Especie, Habitat, MultimediaAnimal, Coordenadas
from django.core import serializers
from django.contrib.auth.models import User
import json
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

"""
def mapa(request):
    coordenadas_info = {}
    base_url = f'http://{get_current_site(None).domain}{settings.MEDIA_URL}'
    formatted_imagenes_data = [f"{base_url}{imagen}" for imagen in imagenes_data]

    # Obtener todas las coordenadas y sus datos asociados
    coordenadas = Coordenadas.objects.all()

    for index, coordenada in enumerate(coordenadas):
        info_animal = coordenada.infoAnimal

        # Serializar los modelos para obtener sus datos en forma de diccionario
        animal_data = json.loads(serializers.serialize('json', [info_animal.animal]))[0]['fields'] if info_animal and info_animal.animal else {}
        info_animal_data = json.loads(serializers.serialize('json', [info_animal]))[0]['fields'] if info_animal else {}
        nivel_peligro_data = json.loads(serializers.serialize('json', [info_animal.nivelpeligro]))[0]['fields'] if info_animal and hasattr(info_animal, 'nivelpeligro') else {}
        especie_data = json.loads(serializers.serialize('json', [info_animal.especie]))[0]['fields'] if info_animal and hasattr(info_animal, 'especie') else {}
        habitat_data = json.loads(serializers.serialize('json', [info_animal.habitat]))[0]['fields'] if info_animal and hasattr(info_animal, 'habitat') else {}
        usuario_id = animal_data.get('usuario')
        multimedia_data = json.loads(serializers.serialize('json', [info_animal.multimediaanimal]))[0]['fields'] if hasattr(info_animal, 'multimediaanimal') else {}

        # 
        multimedia_data_with_url = {
                "videos": f"{base_url}{multimedia_data['videos']}",
                "modeloAr": multimedia_data["modeloAr"],
                # ... add other fields as needed
                }

        # Obtención del usuario
        usuario = User.objects.get(id=usuario_id)

        # Crear la estructura de datos que necesitas
        coordenadas_info[index] = {
                "latitud": coordenada.latitud,
                "longitud": coordenada.longitud,
                "informacionAnimal": {
                    "animal": animal_data,
                    "infoAnimal": info_animal_data,
                    "nivelPeligro": nivel_peligro_data,
                    "especie": especie_data,
                    "habitat": habitat_data,
                    "multimedia": multimedia_data_with_url,
                    "imagenes": formatted_imagenes_data,
                    },
                "usuario": usuario
                }

    context = {
            "coordenadas": coordenadas_info
            }
    return render(request, "mapa.html", context)
"""

def mapa(request):
    coordenadas_info = {}

    # Asegurémonos de que el objeto de solicitud (request) no sea None
    if request is not None:
        base_url = f'http://{get_current_site(request).domain}{settings.MEDIA_URL}'
    else:
        base_url = ''

    # Obtener todas las coordenadas y sus datos asociados
    coordenadas = Coordenadas.objects.all()

    for index, coordenada in enumerate(coordenadas):
        info_animal = coordenada.animal

        # Inicializamos multimedia_data_with_url como un diccionario vacío
        multimedia_data_with_url = {}

        # Inicializamos formatted_imagenes_data como una lista vacía
        formatted_imagenes_data = []

        # Serializar los modelos para obtener sus datos en forma de diccionario
        animal_data = json.loads(serializers.serialize('json', [info_animal]))[0]['fields'] if info_animal and info_animal else {}
        info_animal_data = json.loads(serializers.serialize('json', [info_animal]))[0]['fields'] if info_animal else {}
        nivel_peligro_data = json.loads(serializers.serialize('json', [info_animal.nivelpeligro]))[0]['fields'] if info_animal and hasattr(info_animal, 'nivelpeligro') else {}
        especie_data = json.loads(serializers.serialize('json', [info_animal.especie]))[0]['fields'] if info_animal and hasattr(info_animal, 'especie') else {}
        habitat_data = json.loads(serializers.serialize('json', [info_animal.habitat]))[0]['fields'] if info_animal and hasattr(info_animal, 'habitat') else {}
        usuario_id = animal_data.get('usuario')

        # Obtención del usuario
        usuario = User.objects.get(id=usuario_id)


        # Obtención de recursos multimedia (videos, imágenes, icono)
        multimedia = MultimediaAnimal.objects.filter(animal=info_animal).first()
        if multimedia:
            multimedia_data_with_url = {
                    "videos": f"{base_url}{multimedia.videos}",
                    "modeloAr": multimedia.modeloAr,
                    "icono": f"{base_url}{multimedia.icono}" if multimedia.icono else '',
                    "imagen": f"{base_url}{multimedia.imagen}" if multimedia.imagen else '',
                    }

        # Creamos la estructura de datos que necesitas
        coordenadas_info[index] = {
                "latitud": coordenada.latitud,
                "longitud": coordenada.longitud,
                "informacionAnimal": {
                    "animal": animal_data,
                    "infoAnimal": info_animal_data,
                    "nivelPeligro": nivel_peligro_data,
                    "especie": especie_data,
                    "habitat": habitat_data,
                    "multimedia": multimedia_data_with_url,
                    "imagenes": formatted_imagenes_data,
                    },
                "usuario": usuario
                }

    context = {
            "coordenadas": coordenadas_info
            }
    return render(request, "mapa.html", context)
