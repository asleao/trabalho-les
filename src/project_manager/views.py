from django.shortcuts import render

<<<<<<< HEAD
def hello_world(request):
    return render(request, 'base.html')

def cadastro_ferramenta(request):
    return render(request, 'cadastro_ferramenta.html')
=======
def login(request):
    return render(request, 'login.html')

def cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')
>>>>>>> dbd590e5c0b470740786f5bb352a179c8fe68feb
