from django.db import models
from ckeditor.fields import RichTextField
from apps.usuario.models import User

# Create your models here.


class Blog(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    contenido = RichTextField(verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    reportada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pagina = models.ForeignKey(Blog, on_delete=models.CASCADE) 