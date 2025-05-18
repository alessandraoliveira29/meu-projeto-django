from django.contrib import admin
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'ano_criacao')  # colunas visíveis
    search_fields = ('nome', 'genero')                # campo de busca
    list_filter = ('genero', 'ano_criacao')           # filtros laterais
    ordering = ('nome',)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'ano_lancamento')
    search_fields = ('titulo', 'banda__nome')           # pesquisa por nome da banda também
    list_filter = ('ano_lancamento', 'banda__nome')     # filtros
    ordering = ('banda', 'ano_lancamento')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao')
    search_fields = ('titulo', 'album__titulo')         # permite buscar por título do álbum
    list_filter = ('album__banda__nome',)               # filtrar por nome da banda da música
    ordering = ('album', 'titulo')

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
