from django.db import models

# Creamos el modelo social:
class Link(models.Model):
    key = models.SlugField(verbose_name = 'Nombre clave', max_length=100, unique=True) # Este tipo de campo nos obliga a utilizar caracteres alfanuméricos, guiones o barras. Perfecto para utilizar como clave
    name = models.CharField(verbose_name="Red social", max_length=200) 
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["-created"]

    def __str__(self):
        return self.name
