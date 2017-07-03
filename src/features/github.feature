#language: pt

Funcionalidade: Integração GitHub
Contexto:
Dado possuo usuarios cadastrados no sistema
E possuo a ferramenta do Github cadastrada no sistema
E possuo linguagens cadastradas no sistema
E possuo credencial cadastrada do usuario root
E possuo projetos cadastrados no sistema

Cenário: Cadastrar projeto no GitHub

Quando chamo a funcao cadastrar projeto
Então O projeto é cadastrado no Github
E recebo um retorno http 200 da request
