from django import forms
from django.forms import inlineformset_factory
from .models import Projeto, Tecnologia, ImagemProjeto, DetalhesTecnicos

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'titulo', 'descricao',
            'link_github', 'link_demo',
            'conceitos_aplicados', 'desafios_interessantes',
            'disciplina'
        ]

TecnologiaFormSet = inlineformset_factory(
    Projeto,
    Projeto.tecnologias.through,
    fields=['tecnologia'],
    extra=1,
    can_delete=True
)

ImagemFormSet = inlineformset_factory(
    Projeto,
    ImagemProjeto,
    fields=['imagem'],
    extra=1,
    can_delete=True
)

DetalhesFormSet = inlineformset_factory(
    Projeto,
    DetalhesTecnicos,
    fields=['detalhes'],
    extra=1,
    max_num=1,
    can_delete=True
)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']
