# Django - Projeto de Exemplo

Este repositório contém um projeto básico desenvolvido com o framework Django, que demonstra uma estrutura típica de aplicação web em Python.

## Tecnologias Utilizadas

- Python  
- Django  
- MySQL

## Estrutura do Projeto

.
├── manage.py
├── projeto_django/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── app/
│ ├── init.py
│ ├── models.py
│ ├── views.py
└── requirements.txt


- `manage.py`: Script para gerenciamento do projeto (migrations, servidor, etc).  
- `projeto_django/`: Configurações principais do projeto Django.  
- `app/`: Aplicação Django com modelos e views.  
- `MySQL`: Banco de dados MySQL local.  
- `requirements.txt`: Lista de dependências do projeto.

## Como Executar

1. Clone o repositório:
   git clone https://github.com/Rafael-smr/Django.git
   cd Django

2. Crie e ative um ambiente virtual:
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute as migrações do banco de dados:
    python manage.py migrate

5. Inicie o servidor de desenvolvimento:
    python manage.py runserver

6. Acesse o projeto pelo navegador:
    http://localhost:8000

## Contribuições
Contribuições são bem-vindas! Abra uma issue ou envie um pull request para melhorias, correções ou novas funcionalidades.