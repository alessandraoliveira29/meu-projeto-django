from django.db import models
from datetime import timedelta

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_criacao = models.IntegerField()
    nacionalidade = models.CharField(max_length=50, blank=True, default='')
    foto = models.ImageField(upload_to='bandas_fotos/', null=True, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    capa = models.ImageField(upload_to='capas_albuns/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    titulo = models.CharField(max_length=100)
    duracao = models.DurationField()  
    letra = models.TextField(blank=True)
    link_spotify = models.URLField(blank=True)
    link_youtube = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
