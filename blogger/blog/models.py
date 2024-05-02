from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
