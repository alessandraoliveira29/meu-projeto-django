import os
import django
from datetime import timedelta
from django.db.models import Count, Avg

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from bandas.models import Banda, Album, Musica
from django.db.models import Count

def run_queries():
    print("\n--- Pergunta 1: Listar o nome das bandas, ordenadas alfabeticamente ---")
    bandas_ordenadas = Banda.objects.all().order_by('nome')
    for b in bandas_ordenadas:
        print(b.nome)

    print("\n--- Pergunta 2: Listar o nome dos álbuns de uma banda (Queen), ordenados cronologicamente ---")
    try:
        queen = Banda.objects.get(nome="Queen")
        albuns_queen = Album.objects.filter(banda=queen).order_by('ano_lancamento')
        for alb in albuns_queen:
            print(f"{alb.titulo} - {alb.ano_lancamento}")
    except Banda.DoesNotExist:
        print("Banda 'Queen' não encontrada")

    print("\n--- Pergunta 3: Apresentar todos os álbuns lançados entre 1970 e 1980 ---")
    albuns_70s = Album.objects.filter(ano_lancamento__range=(1970, 1980))
    for alb in albuns_70s:
        print(f"{alb.titulo} ({alb.ano_lancamento}) - {alb.banda.nome}")

    print("\n--- Pergunta 4: Exibir a média de duração das músicas do álbum 'Abbey Road' ---")
    try:
        abbey = Album.objects.get(titulo="Abbey Road")
        # Calculamos a média de 'duracao' e pegamos o valor em 'duracao__avg'
        avg_duration = Musica.objects.filter(album=abbey).aggregate(Avg('duracao'))['duracao__avg']
        if avg_duration:
            print(f"Média de duração das faixas de '{abbey.titulo}': {avg_duration}")
        else:
            print(f"Nenhuma música encontrada para '{abbey.titulo}'")
    except Album.DoesNotExist:
        print("Álbum 'Abbey Road' não encontrado")

    print("\n--- Pergunta 5: Listar os álbuns com músicas de duração > 5 min ---")
    albuns_com_longas = Album.objects.filter(musicas__duracao__gt=timedelta(minutes=5)).distinct()
    for a in albuns_com_longas:
        print(f"{a.titulo} ({a.banda.nome})")

    print("\n--- Pergunta 6: Listar todas as músicas que tenham a palavra 'amor' na letra ---")
    musicas_amor = Musica.objects.filter(letra__icontains='amor')
    for m in musicas_amor:
        print(f"{m.titulo} - Álbum: {m.album.titulo}, Banda: {m.album.banda.nome}")

    print("\n--- Pergunta 7: Listar bandas criadas depois de 1990 ---")
    bandas_apos_90 = Banda.objects.filter(ano_criacao__gte=1990)
    for b in bandas_apos_90:
        print(f"{b.nome} (Criada em {b.ano_criacao})")

    print("\n--- Pergunta 8: Listar todas as bandas cujo gênero contenha 'Rock' ---")
    bandas_rock = Banda.objects.filter(genero__icontains='rock')
    for b in bandas_rock:
        print(f"{b.nome} - Gênero: {b.genero}")

    print("\n--- Pergunta 9: Banda criada mais recentemente ---")
    banda_mais_nova = Banda.objects.order_by('-ano_criacao').first()
    if banda_mais_nova:
        print(f"{banda_mais_nova.nome} (Ano criação: {banda_mais_nova.ano_criacao})")
    else:
        print("Nenhuma banda encontrada")

    print("\n--- Pergunta 10: Quantidade de músicas em cada álbum ---")
    albuns_count = Album.objects.annotate(total_musicas=Count('musicas'))
    for alb in albuns_count:
        print(f"{alb.titulo}: {alb.total_musicas} músicas")


if __name__ == "__main__":
    # Executa as queries quando rodar diretamente "python perguntas.py"
    run_queries()
