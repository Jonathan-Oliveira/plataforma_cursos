from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect
from django.http import HttpResponse
import hashlib


def cadastro(request):
    status = request.GET.get('status')
    return render(request, "cadastro.html", {'status': status})


def login(request):
    return render(request, "login.html")


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario_existente = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0 or\
            len(senha.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')

    if len(senha) < 8 or len(senha) > 14:
        return redirect('/auth/cadastro/?status=1')

    if len(usuario_existente) > 0:
        return redirect('/auth/cadastro/?status=3')
    try:
        senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha)

        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return HttpResponse("Erro ao cadastrar usuário, tente novamente")