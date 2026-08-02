from fastapi import APIRouter

from app.schemas.task import TaskCreate

router = APIRouter()

tarefas = []

@router.get("/tarefas")

def listar_tarefas():
    return tarefas

#buscar tarefa

@router.get("/tarefas/{id}")

def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

    return {"mensagem": "Tarefa não encontrada"}

#deletar tarefa

@router.delete("/tarefas/{id}")

def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa deletada com sucesso"} 
        
    return {"mensagem": "Tarefa não encontrada"}
        
#atualizar tarefa

@router.put("/tarefas/{id}")

def atualizar_tarefa(id: int, task: TaskCreate):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = task.titulo
            return tarefa

    return {"mensagem": "Tarefa não encontrada"}

        

#criar tarefa

@router.post("/tarefas")

def criar_tarefa(task: TaskCreate):

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": task.titulo,
        "concluida": False
    }

    tarefas.append(tarefa)

    return tarefa