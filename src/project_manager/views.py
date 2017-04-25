from django.shortcuts import render

def hello_world(request):
    return render(request, 'base.html')

def cadastro_ferramenta(request):
    return render(request, 'cadastro_ferramenta.html')
