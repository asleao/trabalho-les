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