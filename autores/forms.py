from django import forms
from .models import Artigo, Comentario, Rating, Autor

class ArtigoForm(forms.ModelForm):
    autor_nome = forms.CharField(
        label="Nome do Autor",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Escreva aqui o nome do autor'})
    )

    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'imagem_capa', 'autor_nome']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows':5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.autor:
            self.fields['autor_nome'].initial = self.instance.autor.nome

    def save(self, commit=True):
        nome = self.cleaned_data.pop('autor_nome').strip()
        autor, _ = Autor.objects.get_or_create(nome=nome)
        self.instance.autor = autor
        return super().save(commit=commit)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome_comentador', 'texto']
        widgets = {'texto': forms.Textarea(attrs={'rows':3})}


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['valor']
        widgets = {'valor': forms.NumberInput(attrs={'min':1, 'max':5})}
