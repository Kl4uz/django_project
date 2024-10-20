from django.contrib import admin
from django.urls import path, include
from .views import home, cadastro, login


urlpatterns = [
    #path('caminho url', função da view, name='apelido para a model')
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name = 'login'),
    path('veiculo/', include('veiculo.urls'), name='veiculo')
    # name = 'nome' é sensivel a Maiúsculo e minusculo!
]
