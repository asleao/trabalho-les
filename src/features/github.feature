#language: pt

Funcionalidade: Integração GitHub
Contexto:
Dado que estou logado no sistema
E possuo projetos cadastrados

Cenário: Cadastrar projeto no GitHub

Quando clico no botão cadastrar projeto
Então Sou redirecionado para a página principal de projetos
E um repositório é criado no github com o nome do projeto
E os participantes são incluidos como colaboradores do projeto

Cenário: adicionar colaboradores ao projeto

Quando clico no botão atualizar participantes
Então Sou redirecionado para a página principal de projetos
E os participantes que forem selecionados no projeto serão adicionados como colaboradores no repositório

Cenário: remover colaboradores do projeto

Quando clico no botão atualizar participantes
Então Sou redirecionado para a página principal de projetos
E os participantes que forem deselecionado não serão mais colaboradores do repositório do projeto