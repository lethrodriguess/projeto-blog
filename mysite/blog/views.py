from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comentario
from .forms import Comentario

# Create your views here.

def base(request):
    postagem = Post.objects.all()
    context = {
        'postagens': postagem
    }
    return render(request, 'base.html', context)

def detail(request, post_id):
    if request.method == 'POST':
        post = request.POST
        comentado = 
    postagem = Post.objects.get(id=post_id)
    comentado = Comentario.objects.filter(post_id = post_id )
    context = {
        'postagens': postagem,
        'comentario': comentado,       
    }
    return render(request, 'detail.html', context)

