from django.shortcuts import render, redirect
from .forms import FormCadastroUsuario
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login


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

    user.save()


    return redirect('/')
