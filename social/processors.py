# Importamos el modelo Link:
from .models import Link

# Creamos una función para definir nuestro diccionario:
def ctx_dict(request):
    ctx = {} # Inicializamos el diccionario vacio.
    links = Link.objects.all() # Recuperamos los datos de la tabla de redes sociales
    # recorremos los datos de las redes sociales y los guardamos en el diccionario ctx:
    for link in links:
        ctx[link.key] = link.url
    return ctx