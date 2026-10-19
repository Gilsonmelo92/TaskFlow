# TaskFlow

API REST para gerenciamento de tarefas, desenvolvida em Python utilizando FastAPI e SQLAlchemy.

O projeto foi desenvolvido com foco em boas práticas de desenvolvimento, organização em camadas, validação de dados, persistência em banco de dados e testes automatizados.

## 🚀 Tecnologias

- Python 3
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn
- Pytest
- Git
- GitHub

## 📋 Funcionalidades

- Criar tarefas
- Listar tarefas com paginação
- Buscar tarefa por ID
- Atualizar tarefas
- Excluir tarefas
- Marcar tarefas como concluídas
- Filtrar tarefas pelo status de conclusão
- Ordenar tarefas por ID, título ou status de conclusão
- Ordenação ascendente (`asc`) e descendente (`desc`)
- Retornar metadados da listagem, incluindo total de tarefas e total de páginas
- Validar os dados recebidos com Pydantic
- Validar títulos, incluindo tamanho mínimo e máximo e remoção de espaços desnecessários
- Rejeitar campos extras nos payloads
- Permitir atualização parcial de tarefas
- Tratar tarefas inexistentes
- Tratar parâmetros de ordenação inválidos
- Testar o comportamento da API com Pytest

## 🏗️ Estrutura do projeto

```text
app/
├── database/
│   ├── database.py
│   └── models.py
├── routers/
│   └── tasks.py
├── schemas/
│   └── task.py
├── services/
│   └── task_service.py
└── main.py

tests/
├── conftest.py
├── test_api.py
├── test_database.py
└── test_tasks.py
```

## 🔄 Arquitetura

O projeto utiliza uma arquitetura em camadas, com separação de responsabilidades:

```text
Cliente
   ↓
Router (FastAPI)
   ↓
Service (lógica da aplicação)
   ↓
SQLAlchemy (acesso aos dados)
   ↓
SQLite
```

### Responsabilidades das camadas

- **Router:** define os endpoints, recebe parâmetros, integra as camadas e converte erros da aplicação em respostas HTTP quando necessário.
- **Service:** concentra as operações da aplicação, as consultas ao banco de dados e as regras de sorting.
- **Schemas:** validam os dados de entrada e definem a estrutura das respostas.
- **Database / Models:** configuram a conexão com o banco de dados e representam as entidades persistidas.
- **Tests:** verificam o comportamento da API, dos services e da camada de persistência.

## 🌐 Endpoints da API

A API disponibiliza operações para criar, listar, consultar, atualizar e excluir tarefas.

| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | `/` | Retorna a mensagem de boas-vindas |
| POST | `/tarefas` | Cria uma tarefa |
| GET | `/tarefas` | Lista tarefas com filtros, sorting e paginação |
| GET | `/tarefas/{id}` | Busca uma tarefa pelo ID |
| PUT | `/tarefas/{id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/{id}` | Exclui uma tarefa |

## 🔎 Listagem, filtros e sorting

O endpoint `GET /tarefas` aceita query parameters para controlar os resultados.

| Parâmetro | Padrão | Descrição |
| --- | --- | --- |
| `page` | `1` | Número da página; mínimo `1` |
| `limit` | `10` | Quantidade de tarefas por página; de `1` a `100` |
| `concluida` | Sem filtro | Filtra por `true` ou `false` |
| `ordenar_por` | `id` | Campo: `id`, `titulo` ou `concluida` |
| `ordem` | `asc` | Direção: `asc` ou `desc` |

### Exemplos de requisições

Listar tarefas:

```http
GET /tarefas
```

Listar a segunda página, com cinco tarefas por página:

```http
GET /tarefas?page=2&limit=5
```

Listar apenas tarefas concluídas:

```http
GET /tarefas?concluida=true
```

Listar tarefas não concluídas:

```http
GET /tarefas?concluida=false
```

Ordenar por título em ordem alfabética:

```http
GET /tarefas?ordenar_por=titulo&ordem=asc
```

Combinar filtro, sorting e paginação:

```http
GET /tarefas?concluida=true&ordenar_por=titulo&ordem=desc&page=1&limit=10
```

### Estrutura da resposta da listagem

A resposta inclui a lista de tarefas e os metadados da paginação:

```json
{
  "tarefas": [
    {
      "id": 1,
      "titulo": "Estudar Python",
      "concluida": false
    }
  ],
  "total": 1,
  "total_paginas": 1
}
```

O exemplo é ilustrativo. Os valores retornados dependem dos dados existentes no banco de dados.

- `tarefas`: tarefas correspondentes aos filtros e à página solicitada.
- `total`: quantidade total de resultados após a aplicação do filtro.
- `total_paginas`: quantidade de páginas disponíveis para os resultados encontrados.

## ⚠️ Validação e tratamento de erros

A API utiliza validação de dados e respostas HTTP adequadas aos diferentes cenários.

| Status HTTP | Significado | Exemplo |
| --- | --- | --- |
| `200 OK` | Requisição executada com sucesso | Listagem ou consulta concluída |
| `201 Created` | Recurso criado | Criação de uma tarefa |
| `400 Bad Request` | Parâmetro inválido segundo uma regra da aplicação | Campo ou direção de sorting inválidos |
| `404 Not Found` | Recurso não encontrado | Consulta, atualização ou exclusão de uma tarefa inexistente |
| `422 Unprocessable Entity` | Dados recebidos não passaram na validação | Título inválido ou campo extra não permitido |

O FastAPI e o Pydantic realizam a validação das requisições, enquanto o router converte erros específicos da aplicação em respostas HTTP. O service mantém as regras da aplicação separadas dos detalhes do protocolo HTTP.

## 🧪 Testes automatizados

O projeto possui testes automatizados utilizando Pytest, organizados em arquivos que cobrem a API, os services e a camada de banco de dados.

Os testes verificam, entre outros cenários:

- Criação, consulta, atualização e exclusão de tarefas
- Validação de dados e rejeição de campos extras
- Tratamento de recursos inexistentes
- Paginação e metadados da listagem
- Filtros por conclusão
- Ordenação ascendente e descendente
- Combinação de filtros, sorting e paginação
- Comportamento da conexão com o banco de dados

**Último resultado registrado:** 57 testes aprovados.

Para executar a suíte completa:

```bash
python -m pytest -v
```

Os testes utilizam um banco de dados separado do banco principal da aplicação, evitando que os testes alterem os dados reais do desenvolvimento.

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Gilsonmelo92/TaskFlow.git
```

### 2. Entrar na pasta

```bash
cd TaskFlow
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

<http://127.0.0.1:8000>

A documentação interativa do FastAPI pode ser acessada pelo Swagger:

<http://127.0.0.1:8000/docs>

A documentação alternativa está disponível em:

<http://127.0.0.1:8000/redoc>

## 🎯 Objetivo do projeto

O TaskFlow faz parte do meu processo de desenvolvimento de competências em desenvolvimento backend com Python.

O objetivo é construir uma aplicação prática aplicando conceitos de:

- Desenvolvimento de APIs REST
- Python e FastAPI
- Validação com Pydantic
- Persistência de dados com SQLAlchemy e SQLite
- Arquitetura em camadas e separação de responsabilidades
- Tratamento de erros HTTP
- Testes automatizados com Pytest
- Controle de versão com Git e GitHub

O projeto é desenvolvido de forma incremental, com implementação de funcionalidades, testes, revisão de código e documentação.

## 👨‍💻 Autor

Gilson Melo

GitHub: <https://github.com/Gilsonmelo92>
