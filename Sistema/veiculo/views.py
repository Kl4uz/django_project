from django.shortcuts import render, redirect
from .models import Veiculo
from django.http import Http404, FileResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy

def ListarVeiculos(request):
    
    if request.method == 'GET':
        model = Veiculo.objects.all()
        return render(request, 'veiculo/list.html', {'veiculos': model})
    
    else:
        action = request.POST.get('create')

        if action:
            return HttpResponse('criar-veiculos')

# def CriarVeiculos(request):
