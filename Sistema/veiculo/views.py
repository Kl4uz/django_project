from django.shortcuts import render, redirect
from .models import Veiculo
from django.http import Http404, FileResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,FormView
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from .serializer import SerializadorVeiculo
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

class ListarVeiculos(ListView):

    template_name = 'veiculo/list.html'
    model = Veiculo
    context_object_name = 'veiculo'
    
    # if request.method == 'GET':
    #     model = Veiculo.objects.all()
    #     return render(request, 'veiculo/list.html', {'veiculos': model})
        
    
def CriarVeiculos(request):
    return render(request, 'veiculos/criar.html')


class APIListarVeiculos(ListAPIView):
#View para listar instâncias de veiculos(por meio da APi REST)

    serializer_class = SerializadorVeiculo
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Veiculo.objects.all()
