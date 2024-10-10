from django.contrib import admin
from django.urls import path
from veiculo.views import cadastro, login, home

urlpatterns = [
    #path('caminho url', função da view, name='apelido para a model')
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    # name = 'nome' é sensivel a Maiúsculo e minusculo!
]
