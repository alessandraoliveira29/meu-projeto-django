# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('cv/', views.cv_view, name='cv'),
    path('projetos/', views.ProjetoList.as_view(), name='proj_list'),
    path('projetos/novo/', views.ProjetoCreate.as_view(), name='proj_create'),
    path('projetos/<int:pk>/editar/', views.ProjetoUpdate.as_view(), name='proj_update'),
    path('projetos/<int:pk>/remover/', views.ProjetoDelete.as_view(), name='proj_delete'),
    path('register/',
          portfolio_views.register_view,
          name='register'),
    path('login/',
          auth_views.LoginView.as_view(
              template_name='portfolio/auth/login.html'
          ),
          name='login'),
     path('logout/',
          auth_views.LogoutView.as_view(
              # opcional: podes criar um logout.html se quiseres mostrar mensagem
              template_name='portfolio/auth/logged_out.html'
          ),
          name='logout'),
                                 name='logout'),
]
