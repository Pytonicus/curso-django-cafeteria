from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    # Añadimos el parametro category_id en la ruta que lo recibiremos en la vista:
    path('category/<int:category_id>/', blog_views.category, name="category")
]
