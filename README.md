# tcc

## Requisitos

- Ter o docker instalado no computador

## Tutorial para reproduzir a prova de conceito apresentada no trabalho

- Rodar `docker compose -f /path-to-the-root-of-this-repo/docker-compose.yml up` e esperar o container levantar, instalar as dependências e rodar as migrações do banco de dados
- Rodar `docker exec -it tcc-api bash -c "./sample_app/manage.py create_data"` e esperar os dados de teste serem criados

Pronto! Acessando http://localhost:8000/graphql/ é possível utilizar uma interface de usuário para realizar as requisições GraphQL desejadas.

Obs.: no arquivo `sample_app/sample_app/schema.py` é possível comentar/descomentar algumas linhas, assim como foi descrito no trabalho, para se reproduzir os cenários com e sem o uso das funcionalidades introduzidas pelo trabalho de extensão.
