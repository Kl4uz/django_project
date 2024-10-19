from django.shortcuts import render, redirect
from .models import Veiculo
from django.http import Http404, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def listarveiuculos(request):
    render(request, 'home.html')