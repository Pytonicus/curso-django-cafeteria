# importamos la librería template y el modelo Page:
from django import template
from pages.models import Page

# Esto es un decorador que creará una nueva funcionalidad:
register = template.Library()

# Utilizamos el decorador que hemos registrado para guardar este método:
@register.simple_tag
def get_page_list(): # Con un metodo recuepramos las páginas:
    pages = Page.objects.all()
    return pages