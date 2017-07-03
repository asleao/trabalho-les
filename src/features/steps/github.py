from features.factories.user import UserFactory
from features.factories.linguagem import LinguagemFactory
from features.factories.ferramenta import FerramentaFactory
from django.contrib.auth.models import User
from project_manager.models import *


@given(u'que estou logado no sistema')
def step_impl(context):
    pass
    '''user = User.objects.get(username='admin')
    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)

    br.find_element_by_name('username').send_keys('admin')
    br.find_element_by_name('password').send_keys('admin123')
    br.find_element_by_name('submit').click()
    br.get_screenshot_as_file('/tmp/screenshot.png')
    assert user.username == "user_000"
    '''

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


def cadastra_projeto(nome_projeto):
    nome = nome_projeto
    ferramentas = cria_ferramentas()
    salva_ferramentas(ferramentas)
    participantes = cria_particiantes()
    salva_participantes(participantes)
    linguagem = LinguagemFactory()
    linguagem.save()
    dono = User.objects.get(username='user_000')
    projeto = Projeto.objects.create(nome=nome, dono=dono, linguagem=linguagem)
    projeto.ferramentas = ferramentas
    projeto.participantes = participantes
    projeto.save
    return projeto


@given(u'possuo projetos cadastrados')
def step_impl(context):
    pass
    '''
    projeto1 = cadastra_projeto('Projeto_Behave1')
    projeto2 = cadastra_projeto('Projeto_Behave2')

    assert projeto1.nome == Projeto.objects.get(nome='Projeto_Behave1').nome
    assert projeto2.nome == Projeto.objects.get(nome='Projeto_Behave2').nome
    '''

@when(u'clico no botão cadastrar projeto')
def step_impl(context):
    pass
    '''
    br = context.browser
    br.get(context.base_url + '/project_manager/projeto/')
    #br.get_screenshot_as_file('/tmp/screenshot.png')
    br.find_element_by_name('cadastrar_projeto').click()
    '''

@then(u'Sou redirecionado para a página principal de projetos')
def step_impl(context):
    pass

@then(u'um repositório é criado no github com o nome do projeto')
def step_impl(context):
    pass


@then(u'os participantes são incluidos como colaboradores do projeto')
def step_impl(context):
    pass


@when(u'clico no botão atualizar participantes')
def step_impl(context):
    pass


@then(u'os participantes que forem selecionados no projeto serão adicionados como colaboradores no repositório')
def step_impl(context):
    pass


@then(u'os participantes que forem deselecionado não serão mais colaboradores do repositório do projeto')
def step_impl(context):
    pass
