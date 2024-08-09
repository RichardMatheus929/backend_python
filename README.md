# Projeto

## Principais adições e diferenciais do teste

- Projeto dockerizado
- Validação dos dados que são passados nos endpoints
    - Todos os campos são obrigatórios ao criar uma pessoa
    - Validação de cpf
    - Validação de data de nascimento
    - Verificação se uma pessoa já existe ao tentar atualizar ou deletar pelo id
- Put dinâmico, a lógica do endpoint permite que seja atualizado um único dado ou mais a depender do que for enviado
- Rotas, verbos e status http bem definidos

## Como rodar

Primeiro você precisa está com o docker e o docker-compose instalado no seu linux, ou wsl.

Na raiz do projeto, com o dockerfile e o docker-compose.yml, rode os seguintes comandos. (Perceba que o container do django leva cerca de 10 segundos para ficar pronto)

```docker
docker-compose up -d
```

Esse comando irá inicializar o container, a flag -d é para iniciar desanexado, sem que o docker lhe prenda no terminal do container. Após os status de completed para os dois containeres serem exibidos no terminal rode o próximo comando. 

Agora todas as requisições já podem ser feitas na porta 8000 do localhost.

## Tecnologias

Para o desenvolvimento do projeto backend, utilizei o django em conjunto com o djangorestframework, principais frameworks backend do python. Além disso utilizei o postgres como banco de dados e utilizei o docker para containerizar o projeto. Django é ótimo porque oferece uma estrutura bem organizada e fácil de usar, com um painel de administração que facilita a gestão da aplicação. Já o Django REST Framework é perfeito para criar APIs de forma rápida e prática, com recursos completos que abstraem muita complexidade do desenvolvimento de API. Juntas, essas ferramentas tornam o desenvolvimento mais rápido, simplificam a manutenção e podem ser facilmente escalonadas no futuro.

## Estrutura e arquitetura do banco de dados

O projeto pede uma certa estrutra da tabela pessoa dentro do nosso banco de dados. O django com seus sistema de migrations, permite sincronizar todos os modelos e configurações definidas no código para o banco de dados, além disso, o seu ORM pode cuidar de toda a estrutura de criação, atualização, deleção e seleção de todos os objetos no banco de dados.

Sendo assim, as principais estruturas de tabelas do banco de dados foram integradas ao sistema de migrations do django, como criação de tabelas e suas definições e tipagens de colunas, adição de chave primária, e adição de chave única.

### Procedures

Os scripts de criação de procedures estão no arquivos de migrations do django. Ao rodar o python manage.py migrate, a migration personalizada criada por mim irá rodar os scripts SQL de criação de todas as procedures no banco de dados postgres. As procedures são chamadas a partir do utils.py 

## Estrutura e arquitetura do backend

### utils.py

Módulo responsávle por toda a abstração das conexões com as procedures do banco de dados, é nela que fica as conexões com as procedures, passando os parâmetros necessários para cada query, e retornando o seu respectivo conteúdo.

### exceptions.py

Apenas algumas exceções personalizadas, também estruturadas a partir do django-rest-framework.

### pessoa/view.py

É nela onde fica a principal lógica de requisições de enpoints, tratamento de erros, e retorno de dados. Os dois endpoints do projeto são classes, que possuem métodos para cada verbo http
