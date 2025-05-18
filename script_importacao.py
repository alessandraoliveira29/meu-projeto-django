import os
import django
import json
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Ajuste o nome do seu projeto
django.setup()

from bandas.models import Banda, Album, Musica


def str_to_timedelta(duration_str):
    """
    Converte string 'HH:MM:SS' em um objeto datetime.timedelta
    """
    hours, minutes, seconds = duration_str.split(":")
    return timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))


def importar_bandas(json_file):
    """
    Lê um JSON com bandas, criando/atualizando cada uma.
    Formato exemplo:
    [
      {
        "nome": "The Beatles",
        "genero": "Rock",
        "ano_criacao": 1960,
        "nacionalidade": "Reino Unido",
        "foto": "",
        "descricao": "Banda inglesa formada em Liverpool."
      },
      ...
    ]
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for banda_data in data:
        nome = banda_data["nome"]
        genero = banda_data["genero"]
        ano_criacao = banda_data["ano_criacao"]
        nacionalidade = banda_data["nacionalidade"]

        banda, created = Banda.objects.get_or_create(
            nome=nome,
            defaults={
                'genero': genero,
                'ano_criacao': ano_criacao,
                'nacionalidade': nacionalidade,
                'foto': banda_data.get('foto', ''),
                'descricao': banda_data.get('descricao', '')
            }
        )
        if not created:
            # Atualiza campos se a banda já existia
            banda.genero = genero
            banda.ano_criacao = ano_criacao
            banda.nacionalidade = nacionalidade
            banda.foto = banda_data.get('foto', '')
            banda.descricao = banda_data.get('descricao', '')
            banda.save()

    print(f"Bandas importadas de {json_file} com sucesso!")


def importar_albuns(json_file):
    """
    Lê um JSON com álbuns e músicas:
    [
      {
        "banda": "The Beatles",
        "titulo": "Abbey Road",
        "ano_lancamento": 1969,
        "capa": "",
        "musicas": [
          {
            "titulo": "Come Together",
            "duracao": "00:04:20"
          },
          ...
        ]
      },
      ...
    ]
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for album_data in data:
        nome_banda = album_data["banda"]
        titulo = album_data["titulo"]
        ano_lancamento = album_data["ano_lancamento"]
        capa = album_data.get("capa", "")
        lista_musicas = album_data.get("musicas", [])

        try:
            banda = Banda.objects.get(nome=nome_banda)
        except Banda.DoesNotExist:
            print(f"Banda '{nome_banda}' não encontrada! Pulei o álbum: {titulo}")
            continue

        # Criar/atualizar o álbum
        album, created = Album.objects.get_or_create(
            banda=banda,
            titulo=titulo,
            defaults={
                'ano_lancamento': ano_lancamento,
                'capa': capa
            }
        )
        if not created:
            album.ano_lancamento = ano_lancamento
            album.capa = capa
            album.save()

        # Criar/atualizar músicas
        for musica_data in lista_musicas:
            titulo_m = musica_data["titulo"]
            duracao_str = musica_data["duracao"]
            duracao_td = str_to_timedelta(duracao_str)

            letra = musica_data.get("letra", "")
            link_spotify = musica_data.get("link_spotify", "")
            link_youtube = musica_data.get("link_youtube", "")

            musica, created_m = Musica.objects.get_or_create(
                album=album,
                titulo=titulo_m,
                duracao=duracao_td,
                defaults={
                    'letra': letra,
                    'link_spotify': link_spotify,
                    'link_youtube': link_youtube
                }
            )
            if not created_m:
                musica.letra = letra
                musica.link_spotify = link_spotify
                musica.link_youtube = link_youtube
                musica.save()

    print(f"Álbuns (e músicas) importados de {json_file} com sucesso!")


def importar_tudo():
    """
    Importa primeiro as bandas (bands.json), depois os álbuns (albums.json).
    """
    importar_bandas("bands.json")
    importar_albuns("albums.json")
    print("Importação completa!")
