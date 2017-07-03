from features.factories.user import UserFactory
from features.factories.linguagem import LinguagemFactory
from features.factories.ferramenta import FerramentaFactory
from features.factories.credencial import CredencialFactory
from django.contrib.auth.models import User
from project_manager.models import *
from project_manager.views import *


@given(u'possuo usuarios cadastrados no sistema')
def step_impl(context):
    user_leao = UserFactory(username='asleao', email='andre.sp.leao@gmail.com', password='admin123')
    user_gabriel = UserFactory(username='gabriellmb05', email='gabriel.luiz.mb@gmail.com', password='admin123')
    user_root = UserFactory(username='LEDS', email='ledsifes@gmail.com', password='admin123')

    lista_usuarios = [user_leao, user_gabriel, user_root]

    salva_participantes(lista_usuarios)

    assert len(User.objects.all()) == 3


@given(u'possuo linguagens cadastradas no sistema')
def step_impl(context):
    linguagem = LinguagemFactory(nome='Python')

    linguagem.save()

    assert len(Linguagem.objects.all()) == 1


@given(u'possuo a ferramenta do Github cadastrada no sistema')
def step_impl(context):
    ferramenta = FerramentaFactory(nome='Github', link='www.github.com')
    ferramenta.save()

    assert len(Ferramenta.objects.all()) == 1


@given(u'possuo credencial cadastrada do usuario root')
def step_impl(context):
    user_root = User.objects.get(username='LEDS')
    ferramenta = Ferramenta.objects.get(nome='Github')
    credencial = CredencialFactory(user_name=user_root.username, token='0a4615e6a9fcf24a45a2c0336a6ac8b41f696efd', agente=user_root, ferramenta=ferramenta)

    assert len(Credencial.objects.all()) == 1


@given(u'possuo projetos cadastrados no sistema')
def step_impl(context):
    lista_participantes = []
    lista_participantes.append(User.objects.get(username='asleao'))
    lista_participantes.append(User.objects.get(username='gabriellmb05'))
    projeto = cria_projeto('Projeto Behave Teste', lista_participantes)

    assert len(Projeto.objects.all()) == 1


@when(u'chamo a funcao cadastrar projeto')
def step_impl(context):
    projeto = Projeto.objects.get(nome='Projeto Behave Teste')
    user_root = User.objects.get(username='LEDS')
    ferramenta = Ferramenta.objects.get(nome='Github')
    credencial = Credencial.objects.get(agente=user_root, ferramenta=ferramenta)
    #request = api_github_repositorio_request(projeto.nome, credencial.token, projeto.linguagem)

    #assert request.status_code == 500
    pass


@then(u'O projeto é cadastrado no Github')
def step_impl(context):
    pass


@then(u'recebo um retorno http 200 da request')
def step_impl(context):
    pass


def cria_ferramentas():
    ferramentas = []
    ferramentas.append(FerramentaFactory(nome='Taiga', link='www.taiga.io'))
    ferramentas.append(FerramentaFactory(nome='Github', link='www.github.com'))
    return ferramentas


def salva_ferramentas(ferramentas):
    for ferramenta in ferramentas:
        ferramenta.save


def cria_particiantes():
    participantes = []
    participantes.append(UserFactory())
    return participantes


def salva_participantes(participantes):
    for participante in participantes:
        participante.save()


def cria_projeto(nome_projeto, participantes):
    ferramenta = []
    nome = nome_projeto
    ferramenta.append(Ferramenta.objects.get(nome='Github'))
    linguagem = Linguagem.objects.get(nome='Python')
    dono = User.objects.get(username='LEDS')
    projeto = Projeto.objects.create(nome=nome, dono=dono, linguagem=linguagem)
    projeto.ferramentas = ferramenta
    projeto.participantes = participantes
    projeto.save
    return projeto
