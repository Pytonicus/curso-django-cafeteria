from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name = "Fecha de publicación", default = now)
    image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, verbose_name = "Autor", on_delete = models.CASCADE)
    # Añadimos un nombre relacional a este campo para usarlo en el template:
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title