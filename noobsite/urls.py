# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('sobre/', views.sobre_view),
    path('contato/', views.contato_view),
    path('elogio/', views.elogio_view),
]