from django.db import models
from django.contrib.auth.models import User


class Posteos (models.Model):
    titulo_posteo = models.CharField(max_length=72, unique=True )
    subtitulo_posteo = models.CharField(max_length=72, unique=True )
    posteo = models.TextField(unique=True)
    fecha_posteo = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
      
      
    def __str__(self):
        return f"Titulo {self.titulo_posteo}, Subtitulo {self.subtitulo_posteo},Posteo {self.posteo}, Fecha {self.fecha_posteo}, Autor {self.autor}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"


