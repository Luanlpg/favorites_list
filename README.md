# favorites_list

Aplicativo para gerenciar informações dos funcionários, como nome, e-mail e departamento.


## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/Luanlpg/favorites_list.git`

- Acesse o repositório: `cd favorites_list/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server da API

- Rode as migrações do projeto: `python manage.py migrate`

- Para rodar testes: `python manage.py test`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela API(Use a interface do DRF)

- Acesse a root da API em: `GET - /api/`

- Faça solicitação de token em: `POST - /api/user`
  - Prams(`username:string, first_name:string, last_name:string, email:string`)
<<<<<<< HEAD
    - Obs: Seu token de autenticação será enviado por email
=======
    - Obs: Seu token de autenticação será enviado via email
>>>>>>> 42792c85857ae9d6a183e43cc66d0d7f66cc3f0c

- Faça consulta de cliente em: `GET - /api/<TOKEN>/client/`

- Faça cadastro de cliente em: `POST - /api/<TOKEN>/client/`
  - Prams:(`name:string, email:string`)

- Faça consulta de cliente especifico em: `GET - /api/<TOKEN>/client/<EMAIL-DO-CLIENTE>`

- Faça edição de cliente especifico em: `PATCH - /api/<TOKEN>/client/<EMAIL-DO-CLIENTE>`
  - Prams:(`name:string, email:string`)

- Faça exclusão de cliente especifico em: `DELETE - /api/<TOKEN>/client/<EMAIL-DO-CLIENTE>`

- Faça consulta de produtos em lista de cliente em: `GET - /api/<TOKEN>/client/<EMAIL-DO-CLIENTE>/list`

- Faça cadastro de produto em lista de cliente em: `POST - /api/<TOKEN>/client/<EMAIL-DO-CLIENTE>/list`
  - Prams:(`id:string`)
