from django.shortcuts import render

def cadastro_ferramenta(request):
    return render(request, 'cadastro_ferramenta.html')

def login(request):
    return render(request, 'login.html')

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')

