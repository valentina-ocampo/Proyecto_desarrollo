from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    tipos_genero = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    
    foto_perfil = models.ImageField(upload_to="profiles", null=True, blank=True)
    genero = models.CharField(max_length=1, choices=tipos_genero, verbose_name='Género')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    pais = models.CharField(max_length=20, verbose_name='País')
    ciudad = models.CharField(max_length=30, verbose_name='Ciudad')

    def __str__(self):
        return f'{super().first_name} {super().last_name}'


class Seguidores(models.Model):
    usuario_seguido = models.ForeignKey(User, on_delete=models.CASCADE)
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Seguidor')