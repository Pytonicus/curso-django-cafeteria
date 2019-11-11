from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Mostraremos en el listado de paginas el título y su orden:
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)