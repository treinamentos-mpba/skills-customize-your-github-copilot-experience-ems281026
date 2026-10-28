# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST usando FastAPI para praticar rotas HTTP, validação de dados com modelos Pydantic e respostas com os códigos de status apropriados. Ao final, você poderá testar a API e explorar sua documentação interativa.

## 📝 Tarefas

### 🛠️ Criar a aplicação e as primeiras rotas

#### Descrição
Crie uma aplicação FastAPI para um catálogo de livros. Configure o ambiente, inicie o servidor local e implemente rotas simples para apresentar a API e verificar se ela está funcionando.

#### Requisitos
O programa concluído deve:

- Instalar e importar FastAPI e executar a aplicação com um servidor ASGI, como Uvicorn
- Criar uma rota `GET /` que retorne uma mensagem identificando o catálogo
- Criar uma rota `GET /health` que retorne um status indicando que a API está ativa
- Iniciar a aplicação localmente e acessar as duas rotas pelo navegador ou por um cliente HTTP
- Abrir a documentação interativa gerada em `/docs`


### 🛠️ Implementar operações CRUD para livros

#### Descrição
Expanda a API para permitir cadastrar, consultar, atualizar e remover livros. Nesta atividade, mantenha os dados em uma coleção em memória; eles não precisam persistir após o encerramento do servidor.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic para os dados de um livro, incluindo identificador, título e autor
- Implementar `POST /books` para cadastrar um livro e retornar o livro criado
- Implementar `GET /books` para listar os livros cadastrados e `GET /books/{book_id}` para consultar um livro pelo identificador
- Implementar `PUT /books/{book_id}` para atualizar um livro e `DELETE /books/{book_id}` para removê-lo
- Usar códigos de status HTTP apropriados, incluindo `201 Created` ao criar um livro e `204 No Content` ao removê-lo com sucesso


### 🛠️ Validar entradas e tratar erros

#### Descrição
Torne a API mais confiável validando os dados recebidos e respondendo de forma clara quando uma operação não puder ser concluída.

#### Requisitos
O programa concluído deve:

- Validar os campos do livro com tipos e restrições apropriados, como exigir título e autor não vazios
- Retornar `404 Not Found` quando uma consulta, atualização ou remoção usar um identificador inexistente
- Permitir filtrar os livros por título usando um parâmetro de consulta, sem diferenciar maiúsculas de minúsculas
- Testar os casos de sucesso e de erro pela documentação `/docs` ou por um cliente HTTP
- Confirmar que os exemplos de requisição e resposta aparecem corretamente na documentação interativa
