from fastapi import APIRouter, HTTPException, status
from app.schemas.task import TaskCreate


router = APIRouter()

tarefas = []

# --- LISTAR TAREFAS ---
@router.get("/tarefas")
def listar_tarefas():
    return tarefas

# --- BUSCAR TAREFA ---
@router.get("/tarefas/{id}", status_code=status.HTTP_404_NOT_FOUND)
def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

#    return {"mensagem": "Tarefa não encontrada"}
#    com o importe do HTTPException, podemos retornar um erro 404 caso a tarefa não seja encontrada.

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Tarefa não encontrada"
    )

# --- CRIAR TAREFA ---
@router.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(task: TaskCreate):
    #Gera um novo ID baseado no maior ID existente.
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": task.titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    return nova_tarefa

# --- ATUALIZAR TAREFA ---
@router.put("/tarefas/{id}")
def atualizar_tarefa(id: int, task: TaskCreate):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = task.titulo
            return tarefa

#    return {"mensagem": "Tarefa não encontrada"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Tarefa não encontrada"
    )

        
# --- DELETAR TAREFA ---
@router.delete("/tarefas/{id}")

def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return {
                "mensagem": "Tarefa deletada com sucesso"
            }

#    return {"mensagem": "Tarefa não encontrada"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Tarefa não encontrada"
    )


        
