from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    # torna '' o caminho para a listagem
    path('', views.ArtigoList.as_view(), name='artigo_list'),
    path('novo/', views.ArtigoCreate.as_view(), name='artigo_create'),
    path('<int:pk>/', views.artigo_detail, name='artigo_detail'),
    path('<int:pk>/editar/', views.ArtigoUpdate.as_view(), name='artigo_update'),
    path('<int:pk>/remover/', views.ArtigoDelete.as_view(), name='artigo_delete'),
]