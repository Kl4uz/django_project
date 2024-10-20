from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth  #u can define parses to functions called with same name
from django.contrib.auth.models import User

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

def cadastro(request):
    #Verificando se o metodo html é GET(quando o usuario está fazendo uma requisição) e renderizando o formulário
    if request.method == "GET":
        return render(request, 'cadastro.html')
    #se enviar os dodos do Formulario (Mudando para POST) armazenara variaveis e mostrar mensagem. (minuto 10 video)
    else:
        name = request.POST.get('name') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username = name).first() or User.objects.filter(email = email).first():
            return render(request, 'cadastro.html', context={'mensagem': 'ja existe um usuário com este nome ou email.'})
        
        user = User.objects.create_user(name, email, password)
        user.save()
        
        return redirect('login')

        # if user:
        #     return HttpResponse('OK!')

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
            if user.is_active:
                login_auth(request, user)
                return redirect('veiculo')
        else:
            return HttpResponse('Email ou senha inválidos!')
        



# class Login(View):

#     action = request.POST.get()

#     def get(self, request):
        
#         if User.is_authenticated and User.is_active:
#             return redirect('/veiculo')
#         else:
#             return render(request, '/cadastro', None)


#     def post(self, request):
        
#         name = request.POST.get('name')
#         senha = request.POST.get('password')

#         user = authenticate(request, name=name, password =senha)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('/veiculo')
#             else:
#                 return HttpResponse('User Inativo')
#         else:
#             return redirect('/cadastro')
        