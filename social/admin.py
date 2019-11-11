from django.contrib import admin
# Importamos el modelo Social:
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Vamos a crear un método que recibirá el grupo de usuario en tiempo de ejecución con request:
    def get_readonly_fields(self, request, obj=None):
        # Vamos a comprobar que el usuario no sea admin y le limitamos el cambio de la clave:
        if request.user.groups.filter(name='personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)


