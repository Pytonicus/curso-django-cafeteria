from django.shortcuts import render
# Cargamos el modelo Service:
from .models import Service

def services(request):
    # Y ahora recuperamos los datos mediante consulta ORM:
    services = Service.objects.all() # Le pasamos los datos al template:
    return render(request, 'services/services.html', {'services': services})