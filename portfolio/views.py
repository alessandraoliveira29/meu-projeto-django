# portfolio/views.py

from django.shortcuts import render
from datetime import datetime
from .models import Projeto
from .models import Tecnologia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProjetoForm
from django.shortcuts import redirect
from .forms import (
    ProjetoForm, TecnologiaFormSet,
    ImagemFormSet, DetalhesFormSet
)

def index_view(request):
    data_atual = datetime.now().strftime("%d/%m/%Y")
    return render(request, "portfolio/index.html", {"data": data_atual})

def sobre_view(request):
    data_atual = datetime.now().strftime("%d/%m/%Y")
    return render(request, "portfolio/sobre.html", {"data": data_atual})

def interesses_view(request):
    data_atual = datetime.now().strftime("%d/%m/%Y")
    return render(request, "portfolio/interesses.html", {"data": data_atual})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, "portfolio/tecnologias.html", {"tecnologias": tecnologias})

def cv_view(request):
    return render(request, "portfolio/cv.html")

class ProjetoList(ListView):
    model = Projeto
    template_name = "portfolio/projetos.html"
    context_object_name = "projetos"

class ProjetoCreate(CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/projeto_form.html"
    success_url = reverse_lazy('portfolio:proj_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tec_formset']  = TecnologiaFormSet()
        ctx['img_formset']  = ImagemFormSet()
        ctx['det_formset']  = DetalhesFormSet()
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        tec_fs, img_fs, det_fs = ctx['tec_formset'], ctx['img_formset'], ctx['det_formset']
        if all([tec_fs.is_valid(), img_fs.is_valid(), det_fs.is_valid()]):
            self.object = form.save()
            for fs in (tec_fs, img_fs, det_fs):
                fs.instance = self.object
                fs.save()
            return redirect(self.success_url)
        return self.render_to_response(ctx)

class ProjetoUpdate(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = "portfolio/projeto_form.html"
    success_url = reverse_lazy('portfolio:proj_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.POST:
            ctx['tec_formset'] = TecnologiaFormSet(self.request.POST, instance=self.object)
            ctx['img_formset'] = ImagemFormSet(self.request.POST, self.request.FILES, instance=self.object)
            ctx['det_formset'] = DetalhesFormSet(self.request.POST, instance=self.object)
        else:
            ctx['tec_formset'] = TecnologiaFormSet(instance=self.object)
            ctx['img_formset'] = ImagemFormSet(instance=self.object)
            ctx['det_formset'] = DetalhesFormSet(instance=self.object)
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        tec_fs, img_fs, det_fs = ctx['tec_formset'], ctx['img_formset'], ctx['det_formset']
        if all([tec_fs.is_valid(), img_fs.is_valid(), det_fs.is_valid()]):
            self.object = form.save()
            for fs in (tec_fs, img_fs, det_fs):
                fs.instance = self.object
                fs.save()
            return redirect(self.success_url)
        return self.render_to_response(ctx)

class ProjetoDelete(DeleteView):
    model = Projeto
    template_name = "portfolio/projeto_confirm_delete.html"
    success_url = reverse_lazy('portfolio:proj_list')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projetos')
            return redirect('portfolio:proj_list')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
    return render(request,
                  'portfolio/auth/register.html',
                 {'form': form})
