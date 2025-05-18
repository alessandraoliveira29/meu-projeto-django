from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Projeto
from .forms  import ProjetoForm


def index_view(request):
    return render(request, "portfolio/index.html")


def sobre_view(request):
    return render(request, "portfolio/sobre.html")


def interesses_view(request):
    return render(request, "portfolio/interesses.html")


def tecnologias_view(request):
    return render(request, "portfolio/tecnologias.html")


def cv_view(request):
    return render(request, "portfolio/cv.html")


class ProjetoList(ListView):
    model               = Projeto
    template_name       = "portfolio/projetos.html"
    context_object_name = "projetos"


class ProjetoCreate(LoginRequiredMixin, CreateView):
    model         = Projeto
    template_name = "portfolio/projeto_form.html"
    form_class    = ProjetoForm
    success_url   = reverse_lazy("portfolio:proj_list")


class ProjetoUpdate(LoginRequiredMixin, UpdateView):
    model         = Projeto
    template_name = "portfolio/projeto_form.html"
    form_class    = ProjetoForm
    success_url   = reverse_lazy("portfolio:proj_list")


class ProjetoDelete(LoginRequiredMixin, DeleteView):
    model         = Projeto
    template_name = "portfolio/projeto_confirm_delete.html"
    success_url   = reverse_lazy("portfolio:proj_list")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("portfolio:proj_list")
    else:
        form = UserCreationForm()
    return render(request, "portfolio/auth/register.html", {"form": form})
