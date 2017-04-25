@given(u'que eu clico no botão cadastre-se da tela de Login')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    br.find_element_by_name('cadastrar').click()
    assert br.current_url.endswith('/cadastro')

@when(u'digito o nome, e-mail, matricula, senha e informo minhas credenciais nas ferramentas')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/cadastro')
    br.find_element_by_name('nome').send_keys('Fulano')
    br.find_element_by_name('email').send_keys('fulano@gmail.com')
    br.find_element_by_name('matricula').send_keys('2000bsi0099')
    br.find_element_by_name('password').send_keys('123456')    

@when(u'clico em cadastrar')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cadastrar').click()

@then(u'o usuário é cadastrado')
def step_impl(context):
    usuario = Pessoa.objects.filter(nome='Fulano').exists()
    assert usuario.nome == Fulano

@then(u'recebo uma notificação de “Usuário cadastrado com sucesso”')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then recebo uma notificação de “Usuário cadastrado com sucesso”')

@then(u'sou redirecionado para a página de login.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then sou redirecionado para a página de login.')
