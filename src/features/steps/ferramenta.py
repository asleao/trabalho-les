from behave import given, when, then
from project_manager.models import Ferramenta
from selenium import webdriver
from test.factories.ferramenta import FerramentaFactory

@given(u'que estou na página de cadastro de ferramenta')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/ferramenta')
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/ferramenta/')

@when(u'digito o nome e link')
def step_impl(context):
    br = context.browser
    ferramenta =FerramentaFactory(nome='gitHub', link='github.com')
    ferramenta.save()
    ferramenta = Ferramenta.objects.filter(nome='gitHub')
    assert ferramenta == True

    br.find_element_by_name('nome').send_keys('gitHub')
    br.find_element_by_name('link').send_keys('github.com')

@when(u'clico em cadastrar')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()

@then(u'recebo uma notificação de “Ferramenta cadastrada com sucesso”')
def step_impl(context):
    br = context.browser
    assert  br.find_element_by_name('mensagem') == 'Ferramenta cadastrada com sucesso'


@then(u'sou redirecionado para a página ferramentas')
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/ferramentas/')
