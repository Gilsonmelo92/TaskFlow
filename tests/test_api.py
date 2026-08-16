def test_root(client):
    response = client.get("/")

    assert response.status_code == 200

def test_create_task(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "Aprender testes com FastAPI"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["titulo"] == "Aprender testes com FastAPI"
    assert data["concluida"] is False
    assert data["id"] is not None


def test_list_tasks(client):
    client.post(
        "/tarefas",
        json={
            "titulo": "Tarefa para teste de listagem"
        }
    )

    response = client.get("/tarefas")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["titulo"] == "Tarefa para teste de listagem"
    assert data[0]["concluida"] is False    


def test_get_task(client):
    create_response = client.post(
        "/tarefas",
        json={
            "titulo": "Tarefa para buscar"
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    response = client.get(f"/tarefas/{task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["titulo"] == "Tarefa para buscar"
    assert data["concluida"] is False  


def test_get_task_not_found(client):
    response = client.get("/tarefas/9999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Tarefa não encontrada"      

def test_update_task(client):
    create_response = client.post(
        "/tarefas",
        json={
            "titulo": "Título original"
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_response = client.put(
        f"/tarefas/{task_id}",
        json={
            "titulo": "Título atualizado"
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == task_id
    assert data["titulo"] == "Título atualizado"
    assert data["concluida"] is False  

def test_update_task(client):
    create_response = client.post(
        "/tarefas",
        json={
            "titulo": "Título original"
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_response = client.put(
        f"/tarefas/{task_id}",
        json={
            "titulo": "Título atualizado"
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == task_id
    assert data["titulo"] == "Título atualizado"
    assert data["concluida"] is False

    get_response = client.get(f"/tarefas/{task_id}")

    assert get_response.status_code == 200

    updated_data = get_response.json()

    assert updated_data["id"] == task_id
    assert updated_data["titulo"] == "Título atualizado"


def test_delete_task(client):
    create_response = client.post(
        "/tarefas",
        json={
            "titulo": "Tarefa para deletar"
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/tarefas/{task_id}"
    )

    assert delete_response.status_code == 200

    data = delete_response.json()

    assert data["mensagem"] == "Tarefa deletada com sucesso"

    get_response = client.get(
        f"/tarefas/{task_id}"
    )

    assert get_response.status_code == 404
    assert get_response.json()["detail"] == "Tarefa não encontrada"    


def test_update_task_not_found(client):
    response = client.put(
        "/tarefas/9999",
        json={
            "titulo": "Tentativa de atualização"
        }
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Tarefa não encontrada"   

def test_delete_task_not_found(client):
    response = client.delete("/tarefas/9999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Tarefa não encontrada"

# teste do schema

def test_create_task_title_too_short(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "ab"
        }
    )

    assert response.status_code == 422        


def test_create_task_title_too_long(client):
    titulo = "a" * 101

    response = client.post(
        "/tarefas",
        json={
            "titulo": titulo
        }
    )

    assert response.status_code == 422


def test_create_task_title_only_spaces(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "     "
        }
    )

    assert response.status_code == 422    

def test_create_task_with_extra_field(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "Minha tarefa",
            "campo_inventado": "teste"
        }
    )

    assert response.status_code == 422


def test_create_task_without_title(client):
    response = client.post(
        "/tarefas",
        json={}
    )

    assert response.status_code == 422

def test_list_tasks_empty(client):
    response = client.get("/tarefas")

    assert response.status_code == 200

    data = response.json()

    assert data == []

def test_create_task_strips_whitespace(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "   Estudar FastAPI   "
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["titulo"] == "Estudar FastAPI"    

# testar o TaskResponse


def test_create_task_response_structure(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "Testar estrutura da resposta"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert "titulo" in data
    assert "concluida" in data    

def test_create_task_response_types(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "Testar tipos da resposta"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["titulo"], str)
    assert isinstance(data["concluida"], bool)    

def test_create_tasks_have_different_ids(client):
    response_1 = client.post(
        "/tarefas",
        json={
            "titulo": "Primeira tarefa"
        }
    )

    response_2 = client.post(
        "/tarefas",
        json={
            "titulo": "Segunda tarefa"
        }
    )

    assert response_1.status_code == 201
    assert response_2.status_code == 201

    task_1 = response_1.json()
    task_2 = response_2.json()

    assert task_1["id"] != task_2["id"]


def test_list_multiple_tasks(client):
    client.post(
        "/tarefas",
        json={
            "titulo": "Primeira tarefa"
        }
    )

    client.post(
        "/tarefas",
        json={
            "titulo": "Segunda tarefa"
        }
    )

    client.post(
        "/tarefas",
        json={
            "titulo": "Terceira tarefa"
        }
    )

    response = client.get("/tarefas")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3

    assert data[0]["titulo"] == "Primeira tarefa"
    assert data[1]["titulo"] == "Segunda tarefa"
    assert data[2]["titulo"] == "Terceira tarefa"    

def test_new_task_starts_not_completed(client):
    response = client.post(
        "/tarefas",
        json={
            "titulo": "Nova tarefa"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["concluida"] is False   


def test_update_task_keeps_completed_status(client):
    create_response = client.post(
        "/tarefas",
        json={
            "titulo": "Tarefa original"
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_response = client.put(
        f"/tarefas/{task_id}",
        json={
            "titulo": "Tarefa atualizada"
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["titulo"] == "Tarefa atualizada"
    assert data["concluida"] is False  