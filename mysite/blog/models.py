from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField(default="")
    pub_date = models.DateTimeField('date published')
    imagem = models.ImageField( default="")

class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    com_date = models.DateTimeField('date published')

    