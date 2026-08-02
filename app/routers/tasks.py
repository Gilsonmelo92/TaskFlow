from fastapi import APIRouter

from app.schemas.task import TaskCreate

router = APIRouter()

tarefas = []

@router.get("/tarefas")

def listar_tarefas():
    return tarefas


@router.get("/tarefas/{id}")

def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

    return {"mensagem": "Tarefa não encontrada"}



@router.post("/tarefas")

def criar_tarefa(task: TaskCreate):

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": task.titulo,
        "concluida": False
    }

    tarefas.append(tarefa)

    return tarefa