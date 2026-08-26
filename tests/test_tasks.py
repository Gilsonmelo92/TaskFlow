from fastapi.testclient import TestClient
from app.services import task_service
from app.schemas.task import TaskCreate, TaskUpdate

from app.main import app

#criamos um cliente de teste
client = TestClient(app)


def test_listar_tarefas():
    response = client.get("/tarefas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)#verifica o conteudo da msg


def test_criar_tarefa():
    dados =  {
        "titulo": "Estudar testes automatizados"
    }
    response = client.post("/tarefas", json=dados)# aquisição para prória API

    assert response.status_code == 201

    resposta = response.json()

    assert resposta["id"] is not None #recebe id do banco
    assert resposta["titulo"] == "Estudar testes automatizados"
    assert resposta["concluida"] is False #regra de negócio

#tratamento de erro de validação criado no TaskCreate
def test_criar_tarefa_com_titulo_invalido():
    dados = {
        "titulo": "a"
    }

    response = client.post("/tarefas", json=dados)

    assert response.status_code == 422


def test_criar_tarefa_com_campo_extra():
    dados = {
        "titulo": "Estudar FastAPI",
        "concluida": True
    }

    response = client.post("/tarefas", json=dados)

    assert response.status_code == 422    

def test_buscar_tarefa():
    dados = {
        "titulo": "Tarefa para buscar"
    }

    response_criar = client.post("/tarefas", json=dados)

    assert response_criar.status_code == 201

    tarefa_criada = response_criar.json()

    id_tarefa = tarefa_criada["id"]

    response_buscar = client.get(f"/tarefas/{id_tarefa}")

    assert response_buscar.status_code == 200

    resposta = response_buscar.json()

    assert resposta["id"] == id_tarefa
    assert resposta["titulo"] == "Tarefa para buscar"

def test_buscar_tarefa_inexistente():
    response = client.get("tarefa/99999")

    assert response.status_code == 404

#testar o PUT
def test_atualizar_tarefa():
    dados_criacao = {
        "titulo": "Tarefa original"
    }

    response_criar = client.post(
        "/tarefas",
        json=dados_criacao
    )

    assert response_criar.status_code == 201

    tarefa_criada = response_criar.json()

    id_tarefa = tarefa_criada["id"]

    dados_atualizacao = {
        "titulo": "Tarefa atualizada"
    }

    response_atualizar = client.put(
        f"/tarefas/{id_tarefa}",
        json=dados_atualizacao
    )

    assert response_atualizar.status_code == 200

    resposta = response_atualizar.json()

    assert resposta["id"] == id_tarefa
    assert resposta["titulo"] == "Tarefa atualizada"
    assert resposta["concluida"] is False


def test_atualizar_tarefa_inexistente():
    dados = {
        "titulo": "Tentativa de atualização"
    }

    response = client.put("/tarefa/99999", json=dados)

    assert response.status_code == 404

def test_deletar_tarefa():
    dados = {
        "titulo": "Tarefa para deletar"
    }

    # Criar a tarefa
    response_criar = client.post(
        "/tarefas",
        json=dados
    )

    assert response_criar.status_code == 201

    tarefa_criada = response_criar.json()

    id_tarefa = tarefa_criada["id"]

    # Deletar a tarefa
    response_deletar = client.delete(
        f"/tarefas/{id_tarefa}"
    )

    assert response_deletar.status_code == 200

    resposta = response_deletar.json()

    assert resposta["mensagem"] == "Tarefa deletada com sucesso"

    # Confirmar que a tarefa não existe mais
    response_buscar = client.get(
        f"/tarefas/{id_tarefa}"
    )

    assert response_buscar.status_code == 404

def test_deletar_tarefa_inexistente():
    response = client.delete("/tarefas/99999")

    assert response.status_code == 404    


# testar regra de negocio

def test_atualizar_tarefa_titulo_mantem_status(db):

    # 1. Criar uma tarefa inicialmente não concluída
    tarefa = task_service.criar_tarefa(
        db,
        TaskCreate(titulo="Tarefa original")
    )

    # 2. Marcar a tarefa como concluída
    dados_status = TaskUpdate(
        concluida=True
    )

    tarefa_atualizada = task_service.atualizar_tarefa(
        db,
        tarefa.id,
        dados_status
    )

    # Confirmar que o status foi alterado
    assert tarefa_atualizada.concluida is True

    # 3. Atualizar somente o título
    dados_titulo = TaskUpdate(
        titulo="Novo título"
    )

    tarefa_atualizada = task_service.atualizar_tarefa(
        db,
        tarefa.id,
        dados_titulo
    )

    # 4. Confirmar que o título foi alterado
    assert tarefa_atualizada.titulo == "Novo título"

    # 5. Confirmar que o status permaneceu concluído
    assert tarefa_atualizada.concluida is True