from django.contrib import admin
from .models import Autor, Artigo, Comentario, Rating

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor__nome')
    list_filter = ('data_publicacao',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'nome_comentador', 'data')
    search_fields = ('nome_comentador', 'artigo__titulo')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'valor', 'data')
    list_filter = ('valor',)

admin.site.register(Autor)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Rating, RatingAdmin)
