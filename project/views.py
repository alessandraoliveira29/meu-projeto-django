# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")
    
def sobre_view(request):
    return HttpResponse("Este site foi feito para aprender Django do jeito mais simples possível!")

def contato_view(request):
    return HttpResponse("Para entrar em contato, envie um e-mail para noob@exemplo.com")

def elogio_view(request):
    return HttpResponse("Você é incrível por estar aprendendo Django! Continue assim 😄")