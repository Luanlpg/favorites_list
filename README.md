# favorites_list

Aplicativo para gerenciar informações dos funcionários, como nome, e-mail e departamento.


## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/Luanlpg/favorites_list.git`

- Acesse o repositório: `cd favorites_list/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server da API

- Acesse o projeto django com: `cd favorites`

- Rode as migrações do projeto: `python manage.py migrate`

- Para rodar testes: `python manage.py test`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela API(Use a interface do DRF)

- Acesse a root da API em: `GET - /api/`

- Faça solicitação de token em: `POST - /api/user`
  - Prams(`username:string, first_name:string, last_name:string, email:string`)
    - Obs: Seu token de autenticação será envia por email

- Faça consulta de cliente em: `GET - /api/<token>/client/`

- Faça cadastro de cliente em: `POST - /api/<token>/client/`
  - Prams:(`name:string, email:string`)

- Faça consulta de cliente especifico em: `GET - /api/<token>/client/<Email do cliente>`

- Faça edição de cliente especifico em: `PATCH - /api/<token>/client/<Email do cliente>`
  - Prams:(`name:string, email:string`)

- Faça exclusão de cliente especifico em: `DELETE - /api/<token>/client/<Email do cliente>`

- Faça consulta de produtos em lista de cliente em: `GET - /api/<token>/client/<Email do cliente>/list`

- Faça cadastro de produto em lista de cliente em: `POST - /api/<token>/client/<Email do cliente>/list`
  - Prams:(`id:string`)
