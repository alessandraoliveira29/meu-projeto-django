# portfolio/models.py

from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    docentes = models.CharField(max_length=255)
    link_moodle = models.URLField()
    link_ulusofona = models.URLField()

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/')
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    link_github = models.URLField(blank=True, null=True)
    link_demo = models.URLField(blank=True, null=True)
    conceitos_aplicados = models.TextField()
    desafios_interessantes = models.TextField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo

class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return f"Imagem do projeto: {self.projeto.titulo}"

class DetalhesTecnicos(models.Model):
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)
    detalhes = models.TextField()

    def __str__(self):
        return f"Detalhes técnicos de {self.projeto.titulo}"

class Visitor(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    first_visit = models.DateTimeField(auto_now_add=True)

