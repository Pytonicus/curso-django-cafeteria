# Vamos a cargar un accesor para evitar cuelgues:
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts}) 

def category(request, category_id):
    # Sustituimos la consulta ORM por el accesor y le pasamos el modelo y la consulta que vamos a recuperar:
    category = get_object_or_404(Category, id = category_id)
    return render(request, "blog/category.html", {'category':category})