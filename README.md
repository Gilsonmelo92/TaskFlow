# TaskFlow

API REST para gerenciamento de tarefas, desenvolvida em Python utilizando FastAPI e SQLAlchemy.

O projeto foi desenvolvido com foco em boas práticas de desenvolvimento, organização em camadas, validação de dados, persistência em banco de dados e testes automatizados.

## 🚀 Tecnologias

* Python 3
* FastAPI
* Pydantic
* SQLAlchemy
* SQLite
* Uvicorn
* Pytest
* Git
* GitHub

## 📋 Funcionalidades

* Criar tarefas
* Listar tarefas
* Buscar tarefa por ID
* Atualizar tarefas
* Excluir tarefas
* Marcar tarefas como concluídas
* Validação dos dados recebidos
* Tratamento de tarefas inexistentes
* Bloqueio de campos extras nos payloads
* Validação de títulos
* Atualização parcial de tarefas

## 🏗️ Estrutura do projeto

```text
app/
├── database/
│   ├── database.py
│   └── models.py
│
├── routers/
│   └── tasks.py
│
├── schemas/
│   └── task.py
│
├── services/
│   └── task_service.py
│
└── main.py

tests/
├── conftest.py
├── test_api.py
├── test_database.py
└── test_tasks.py
```

## 🔄 Arquitetura

O projeto utiliza uma separação de responsabilidades entre as principais camadas:

```text
Cliente
   ↓
Router
   ↓
Service
   ↓
SQLAlchemy
   ↓
SQLite
```

Os testes são organizados para validar diferentes partes da aplicação:

```text
Pytest
├── API
├── Services
└── Database
```

## 🧪 Testes

O projeto possui uma suíte de testes automatizados utilizando Pytest.

Estado atual:

**41 testes passando**

Para executar os testes:

```bash
python -m pytest
```

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

A API estará disponível localmente.

A documentação interativa do FastAPI pode ser acessada através do Swagger:

http://127.0.0.1:8000/docs

## 🎯 Objetivo do projeto

O TaskFlow faz parte do meu processo de desenvolvimento de competências em desenvolvimento backend com Python.

O objetivo é construir uma aplicação real aplicando conceitos de:

* Desenvolvimento de APIs REST
* FastAPI
* Python
* Pydantic
* SQLAlchemy
* Bancos de dados
* Arquitetura em camadas
* Testes automatizados
* Git e GitHub

O projeto continuará evoluindo com novas funcionalidades e melhorias de arquitetura.

## 👨‍💻 Autor

Gilson Melo
