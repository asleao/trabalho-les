from features.factories.user import UserFactory


@given(u'que estou logado no sistema')
def step_impl(context):
    user = UserFactory()

    print(user.name)
    pass


@given(u'possuo projetos cadastrados')
def step_impl(context):
    pass


@when(u'clico no botão cadastrar projeto')
def step_impl(context):
    pass


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
