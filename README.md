# Test Company Hero

Essa aplicação faz parte do teste para desenvolvedor para Company Hero, utilizando as tecnologias python, django, postgres e heroku.

A aplicação faz a gravação de usuários no banco PostgreSQL, faz a leitura de todos os documentos, faz a busca por usuário e a busca por empresa.

## Banco de dados:

O banco é composto por duas tabelas (employees e enterprises).

Employees é composta pelos campos:

- username: [string] Nome do usuário (Esse campo é uma chave primária, aceita entradas de até 32 caracteres).
- name: [string] Nome do funcionário (Esse campo aceita entradas de até 200 caracteres).
- age: [int] Idade do funcionário (Somente números inteiros entre 10 e 120 são aceitos).
- enterprise: [list] Lista com o nome das empresas do funcionário.

Enterprises é composta pelos campos:

- name: [string] Nome do usuário (Esse campo é uma chave primária, aceita entradas de até 32 caracteres).
- country: [string] País da empresa (Esse campo é uma chave primária, aceita entradas de até 200 caracteres).

## Gravação de informações da empresa:

Para fazer a gravação de um nova empresa, utilize o método `POST` no link `test-ch-01.herokuapp.com/enterprises/`, passando o arquivo json no formato:

```
{
    "name": "name",
    "country": "country"
}
```

## Gravação de informações do usuário:

Para fazer a gravação de um novo funcionário, utilize o método `POST` no link `test-ch-01.herokuapp.com/employees/`, passando o arquivo json no formato:

```
{
    "username": "username",
    "name": "name",
    "age": int,
    "enterprise": ["enterprise_a","enterprise_b"]
}
```

## Leitura de dados por usuário:

A leitura por user name é feita através do método `GET` no endpoint `test-ch-01.herokuapp.com/username/<username>`.

Exemplo:

- Input:

```
test-ch-01.herokuapp.com/username/t01
```

- Output:

```
{
    "username": "t01",
    "name": "test",
    "age": 50,
    "enterprise": [
        "a",
        "b"
    ]
}
```

## Listagem de dados por empresa:

A leitura por username é feita através do método `GET` no endpoint `test-ch-01.herokuapp.com/enterprise/<enterprise>`.

Exemplo:

- Input:

```
test-ch-01.herokuapp.com/enterprise/c
```

- Output:

```
[
    {
        "username": "t04",
        "name": "test",
        "age": 50,
        "enterprise": [
            "c"
        ]
    },
    {
        "username": "t05",
        "name": "test",
        "age": 5,
        "enterprise": [
            "c"
        ]
    },
    {
        "username": "t06",
        "name": "test",
        "age": 5,
        "enterprise": [
            "a",
            "c"
        ]
    }
]
```

## Instalação de requirements:

```
$ pip install -r requirements.txt
```

## Comando para execução local:

```
$ git clone https://github.com/BrunoASNascimento/Test-Company-Hero
$ cd Test-Company-Hero
$ python manage.py runserver
```

## Comando para deploy:

```
$ git push heroku master
$ heroku ps:scale web=1
```

## Comando para logs web:

```
$ heroku logs --tail
```
