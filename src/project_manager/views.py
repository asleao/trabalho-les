from django.shortcuts import render, redirect
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import requests
import json
from .models import *
from taiga import TaigaAPI

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
    linguagem_gitignore = projeto.linguagem
    r = requests.post('http://localhost:8001/cria_repositorio/', data={'nome_repositorio':nome, 'token':token, 'linguagem':linguagem_gitignore})
    print(r)
    print(user.social_auth.get(provider='github').access_token)
    return HttpResponse('funcionou')

def adiciona_colaboradores(id_projeto, user_root, participantes):
    list_participantes = []
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    colaboradores = participantes
    for colaborador in colaboradores:
        list_participantes.append(colaborador)
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('http://localhost:8001/adiciona_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(list_participantes)})
    return HttpResponse('funcionou')

def remove_colaboradores(id_projeto, user_root, participantes):
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    list_participantes = []
    nome = projeto.nome
    colaboradores = participantes
    for colaborador in colaboradores:
        list_participantes.append(colaborador)
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('http://localhost:8001/remove_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(list_participantes)})
    return HttpResponse('funcionou')

def taiga(request):
    user = User.objects.get(username='gabriellmb05')
    token = user.social_auth.get(provider='github').access_token
    print(token)
    #api = TaigaAPI(token=token, token_type='github')
    #print(api.me())
    return HttpResponse('funcionou')