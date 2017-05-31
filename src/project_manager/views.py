from django.shortcuts import render, redirect
from .forms import FormCadastroUsuario
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import requests
import json
from .models import *

def cadastro_ferramenta(request):
    return render(request, 'cadastro_ferramenta.html')


def login(request):
    return render(request, 'login.html')

@csrf_protect
def cadastro_usuario(request):
    if request.method == 'POST':
    	form = FormCadastroUsuario(request.POST)
    	if form.is_valid():
            nome = form.cleaned_data['first_name']
            sobrenome = form.cleaned_data['last_name']
            matricula = form.cleaned_data['username']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['password']
            user = User.objects.create_user(matricula, email, senha)
            user.last_name=sobrenome
            user.first_name=nome
            user.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
    	form = FormCadastroUsuario()

    return render(request, 'cadastro_usuario.html',{'form':form})

def autoriza_usuario(request):
    user = request.user
    user.is_superuser = True
    user.is_staff = True

    print(user.social_auth.get(provider='github').access_token)
    user.save()


    return redirect('/')

def cria_repositorio(id_projeto, user_root):
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    token = user.social_auth.get(provider='github').access_token
    linguagem_gitignore = 'Python'
    r = requests.post('http://localhost:8001/cria_repositorio/', data={'nome_repositorio':nome, 'token':token, 'linguagem':linguagem_gitignore})
    print(r)
    print(user.social_auth.get(provider='github').access_token)
    return HttpResponse('funcionou')

def adiciona_colaboradores(id_projeto, user_root):
    list_participantes = []
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    colaboradores = list(projeto.participantes.all())
    for colaborador in colaboradores:
        list_participantes.append(colaborador.username)
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('http://localhost:8001/adiciona_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(list_participantes)})
    return HttpResponse('funcionou')

def remove_colaboradores(request):
    user = request.user
    nome = 'teste_add_collaborator'
    colaboradores = {'usuario1':'asleao', 'usuario2':'paulossjunior'}
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('http://localhost:8001/remove_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(colaboradores)})
    return HttpResponse('funcionou')

