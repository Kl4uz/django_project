from django.urls import path
from .views import ListarVeiculos, CriarVeiculos, SerializadorVeiculo, APIListarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='veiculo'),
    path('criar-veiculo', CriarVeiculos, name='criar-veiculo'),
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculo')
]
