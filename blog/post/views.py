from django.shortcuts import render

# ------- 12
# Importamos Nuestro modelo para poderle pasar datos a nuestras vistas

from .models import Posts

# Create your views here.

# ------- 11
# Definimos nuestras vistas para poder renderizar nuestros html

def Index(request):
    return render(request, 'index.html')

def Blog_list(request):
    query = Posts.objects.all()
    return render(request, 'blog.html', {'posts':query})

def Blog_Detail(request, pk):
    query = Posts.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'body':query})
