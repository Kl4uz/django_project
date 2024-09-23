from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    #Verificando se o metodo html é GET(quando o usuario está fazendo uma requisição) e renderizando o formulário
    if request.method == "GET":
        return render(request, 'cadastro.html')
    #se enviar os dodos do Formulario (Mudando para POST) armazenara variaveis e mostrar mensagem. (minuto 10 video)
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse('dados enviados ' + name + '!')



def login(request):
    return render(request, 'login.html')