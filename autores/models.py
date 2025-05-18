from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='autores_fotos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='artigos')
    imagem_capa = models.ImageField(upload_to='capas_artigos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    nome_comentador = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentário por {self.nome_comentador}"

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    valor = models.IntegerField()  # de 1 a 5
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Rating {self.valor} para {self.artigo.titulo}"
