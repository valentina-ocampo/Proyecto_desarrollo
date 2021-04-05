from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    genres_types = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    
    foto_perfil = models.ImageField(upload_to="profiles", null=True, blank=True)
    genre = models.CharField(max_length=1, choices=genres_types, verbose_name='Género')
    balance = models.PositiveIntegerField(default=0, verbose_name='Saldo')
    telephone = models.CharField(max_length=10, verbose_name='Teléfono')
    country = models.CharField(max_length=20, verbose_name='País')
    city = models.CharField(max_length=30, verbose_name='Ciudad')

    def __str__(self):
        return f'{super().first_name} {super().last_name}'


class Seguidores(models.Model):
    Usuario_seguido = models.ForeignKey(User, on_delete=models.CASCADE)
    Seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Seguidor')