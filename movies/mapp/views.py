from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Models

from .models import *
from .forms import *


# Class Auth
from django.contrib.auth.mixins import LoginRequiredMixin

# Class CBV
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.views import LoginView

# Create your views here.

class HomeView(TemplateView):
    template_name = "mapp/index.html"

class CompanyList(ListView):
    model = Company 

    #def get_queryset(self):
    #    return Company.objects.all().order_by('id').values()

    #def get_queryset(self):
    #    return Company.objects.filter(name__icontains='i').order_by('id').values()


class GenderList(ListView):
    model = Gender

class MovieList(ListView):
    model = Movie

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("home")

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("home")    

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy("home")       

class MyLoginView(LoginView):
    redirect_authenticated_user = True  

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o password Inválidos")
        return super().form_invalid(form)