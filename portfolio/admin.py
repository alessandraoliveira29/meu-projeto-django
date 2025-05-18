from django.contrib import admin
from .models import Disciplina, Tecnologia, Projeto, ImagemProjeto, DetalhesTecnicos

admin.site.register(Disciplina)
admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(ImagemProjeto)
admin.site.register(DetalhesTecnicos)
