from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')
