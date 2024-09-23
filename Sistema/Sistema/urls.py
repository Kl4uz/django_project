from django.contrib import admin
from django.urls import path
from views import cadastro, login

urlpatterns = [
    #path('caminho url', função da view, name='apelido para a model')
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='Cadastro'),
    path('login/', login, name='Login'),
]
