from django.db import models
from django.contrib.auth.models import User

class InformacionAdicionalUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntuacion = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

    def __str__(self):
        return f'Descripcion adicional de {self.user.username}'
