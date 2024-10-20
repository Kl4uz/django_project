from django.urls import path
from .views import ListarVeiculos

urlpatterns = [
    path('' , ListarVeiculos, name='veiculo')
    
]
