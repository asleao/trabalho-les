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

def criar_projeto_ferramenta(projeto_obj, ferramenta_obj):
        nome_projeto = projeto_obj.nome
        participantes = list(projeto_obj.participantes.all())
        user_root = User.objects.get(username='LEDS')
        participantes_username = []
        participantes_email = []
        for participante in participantes:
            participantes_email.append(participante.email)
            participantes_username.append(participante.username)
        print(ferramenta_obj.nome)
        if ferramenta_obj.nome == 'Github':
                cria_repositorio_github(projeto_obj.id, user_root)
                adiciona_colaboradores_github(projeto_obj.id, user_root, participantes_username)
        elif(ferramenta_obj.nome == 'Taiga'):
                cria_projeto_taiga(projeto_obj.id, user_root)
                adiciona_colaboradores_taiga(projeto_obj.id, user_root, participantes_email)
        else:
                print('ferramenta inválida!')

def cria_repositorio_github(id_projeto, user_root):
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    token = user.social_auth.get(provider='github').access_token
    linguagem_gitignore = projeto.linguagem
    r = requests.post('https://api-git.herokuapp.com/cria_repositorio/', data={'nome_repositorio':nome, 'token':token, 'linguagem':linguagem_gitignore})
    print(r)
    return HttpResponse('funcionou')

def adiciona_colaboradores_github(id_projeto, user_root, participantes):
    list_participantes = []
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    colaboradores = participantes
    for colaborador in colaboradores:
        list_participantes.append(colaborador)
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('https://api-git.herokuapp.com/adiciona_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(list_participantes)})
    print(r)
    return HttpResponse('funcionou')

def remove_colaboradores_github(id_projeto, user_root, participantes):
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    list_participantes = []
    nome = projeto.nome
    colaboradores = participantes
    for colaborador in colaboradores:
        list_participantes.append(colaborador)
    token = user.social_auth.get(provider='github').access_token
    r = requests.post('https://api-git.herokuapp.com/remove_colaboradores/', data={'nome_repositorio':nome, 'token':token, 'colaboradores':json.dumps(list_participantes)})
    print(r)
    return HttpResponse('funcionou')

def cria_projeto_taiga(id_projeto, user_root):
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    ferramenta_taiga = Ferramenta.objects.get(nome='Taiga')
    token = Credencial.objects.get(agente=user, ferramenta=ferramenta_taiga).token
    print(nome)
    print(token)
    r = requests.post('https://api-taiga.herokuapp.com/criar_projeto/', data={'nome_projeto':nome, 'token':token})
    print(r)
    return HttpResponse('funcionou')

def adiciona_colaboradores_taiga(id_projeto, user_root, participantes):
    list_participantes = []
    user = user_root
    projeto = Projeto.objects.get(pk=id_projeto)
    nome = projeto.nome
    colaboradores = participantes
    for colaborador in colaboradores:
        list_participantes.append(colaborador)
    print(list_participantes)
    ferramenta_taiga = Ferramenta.objects.get(nome='Taiga')
    token = Credencial.objects.get(agente=user, ferramenta=ferramenta_taiga).token
    r = requests.post('https://api-taiga.herokuapp.com/adicionar_colaboradores/', data={'nome_projeto':nome, 'token':token, 'usernames':json.dumps(list_participantes)})
    print(r)
    return HttpResponse('funcionou')

