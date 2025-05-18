from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Avg

from .models import Artigo
from .forms import ArtigoForm, ComentarioForm, RatingForm

class ArtigoList(ListView):
    model = Artigo
    template_name = "artigos/artigo_list.html"
    context_object_name = "artigos"

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.order_by('-data')
    media = artigo.ratings.aggregate(Avg('valor'))['valor__avg'] or 0

    com_form  = ComentarioForm()
    rate_form = RatingForm()

    if request.method == 'POST':
        if 'comentario_submit' in request.POST:
            com_form = ComentarioForm(request.POST)
            if com_form.is_valid():
                c = com_form.save(commit=False)
                c.artigo = artigo
                c.save()
                return redirect('artigos:artigo_detail', pk=pk)
        elif 'rating_submit' in request.POST:
            rate_form = RatingForm(request.POST)
            if rate_form.is_valid():
                r = rate_form.save(commit=False)
                r.artigo = artigo
                r.save()
                return redirect('artigos:artigo_detail', pk=pk)

    return render(request, "artigos/artigo_detail.html", {
        'artigo': artigo,
        'comentarios': comentarios,
        'media': media,
        'com_form': com_form,
        'rate_form': rate_form,
    })

class ArtigoCreate(CreateView):
    model = Artigo
    form_class = ArtigoForm
    template_name = "artigos/artigo_form.html"
    success_url = reverse_lazy('artigos:artigo_list')

class ArtigoUpdate(UpdateView):
    model = Artigo
    form_class = ArtigoForm
    template_name = "artigos/artigo_form.html"
    success_url = reverse_lazy('artigos:artigo_list')

class ArtigoDelete(DeleteView):
    model = Artigo
    template_name = "artigos/artigo_confirm_delete.html"
    success_url = reverse_lazy('artigos:artigo_list')
