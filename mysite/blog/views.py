from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comentario

# Create your views here.

def base(request):
    postagem = Post.objects.all()
    comentado = Comentario.objects.all()
    context = {
        'postagens': postagem,
        'comentario': comentado,
    }
    return render(request, 'base.html', context)

def detail(request, post_id):
    postagem = Post.objects.all()
    comentado = Comentario.objects.all()
    context = {
        'postagens': postagem,
        'comentario': comentado,
    }
    return render(request, 'detail.html', context)

