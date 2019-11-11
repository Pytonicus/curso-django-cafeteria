from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # Ahora añadimos el post cateogires. 
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name') # La coma siempre es necesaria aunque solo haya un campo o dará error.
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    # Podemos definir nuestros propios campos:
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")]) # Vamos a crear un listado de categorías.
    # Cambiamos el nombre del metodo para que imprima lo que queramos en lugar de post categories:
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)