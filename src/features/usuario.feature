#language: pt

Funcionalidade: Controle de Usuário
Contexto: 
Dado que eu clico no botão cadastre-se da tela de Login

Cenário: Cadastrar Usuário com sucesso

Quando digito o nome, e-mail, matricula, senha e informo minhas credenciais nas ferramentas
E clico em cadastrar
Então o usuário é cadastrado
E recebo uma notificação de “Usuário cadastrado com sucesso” 
E sou redirecionado para a página de login.