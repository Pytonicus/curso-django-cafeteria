from django.contrib import admin
# Importamos la librería models el service:
from .models import Service

# Hacemos de solo lectura los campos de fecha:
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registramos el modelo service en el panel:
admin.site.register(Service, ServiceAdmin)
