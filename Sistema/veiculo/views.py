from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth  #u can define parses to functions called with same name
from django.contrib.auth.models import User

def cadastro(request):
    #Verificando se o metodo html é GET(quando o usuario está fazendo uma requisição) e renderizando o formulário
    if request.method == "GET":
        return render(request, 'cadastro.html')
    #se enviar os dodos do Formulario (Mudando para POST) armazenara variaveis e mostrar mensagem. (minuto 10 video)
    else:
        name = request.POST.get('name') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse("OK!")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        senha = request.POST.get('password')

        #verifica se o usuário existe, se não user == None
        user = authenticate(username = name, password = senha)

        if user:
            #autentica o user logado
            login_auth(request, user)
            return HttpResponse('Login efetuado ' + name + '!')
        else:
            return HttpResponse('Email ou senha inválidos!')
    
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        log = request.POST.get('login')
        cadastro = request.POST.get('cadastro')
    
    if log:
        return redirect('login')
    else:
        return redirect('cadastro')