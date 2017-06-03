@given(u'que estou logado no sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    br.find_element_by_name('login-github').click()
    if br.current_url.endswith('/') != True:
        br.find_element_by_id('login_field').send_keys('leds')
        br.find_element_by_id('password').send_keys('leds2013ifesbr')
        br.find_element_by_name('commit').click()
        if br.current_url.endswith('/') != True:

            br.find_element_by_name('authorize').click()
    assert br.current_url.endswith('/')

@given(u'possuo projetos cadastrados')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given possuo projetos cadastrados')

@when(u'clico no botão cadastrar projeto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão cadastrar projeto')

@then(u'Sou redirecionado para a página principal de projetos')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Sou redirecionado para a página principal de projetos')

@then(u'um repositório é criado no github com o nome do projeto')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then um repositório é criado no github com o nome do projeto')

@then(u'os participantes são incluidos como colaboradores do projeto')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then os participantes são incluidos como colaboradores do projeto')
