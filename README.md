# GitHub User Report

Este é um programa que faz requisições à API do GitHub e gera um relatório em um arquivo de texto com informações do usuário e seus repositórios.

## Como usar

1. Clone ou faça o download do repositório.
2. Certifique-se de ter o Python 3.x instalado em seu sistema.
3. Instale o pacote requests, caso ainda não o tenha instalado, com o seguinte comando: pip install requests
4. O relatório gerado estará disponível na pasta do projeto, com o nome sendo o nick do usuário seguido de .txt.

## Como funciona

A classe User é responsável por armazenar as informações do usuário que são obtidas através da API do GitHub.

A função obter_user faz uma requisição à API do GitHub com o nome de usuário passado como parâmetro e retorna um objeto User com as informações recebidas.

A função obter_user_repos faz uma requisição à API do GitHub e retorna um dicionário com os nomes e URLs dos repositórios do usuário.

A função user_report gera um relatório em um arquivo de texto com informações do usuário e seus repositórios. O nome do arquivo é baseado na última parte da URL do perfil do usuário.

O módulo unittest é utilizado para testar se a classe User possui os atributos mínimos necessários, se a função obter_user retorna None quando é feita uma requisição inválida, se a função obter_user_repos retorna um dicionário e se ele tem mais de um item, e se o relatório gerado pela função user_report contém informações básicas do usuário e dos repositórios.
