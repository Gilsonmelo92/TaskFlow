from fastapi import APIRouter, HTTPException, status
from app.schemas.task import TaskCreate
from app.services import task_service


router = APIRouter()

# --- LISTAR TAREFAS ---
@router.get("/tarefas")
def listar_tarefas():
    return task_service.listar_tarefas()
#    return tarefas

# --- BUSCAR TAREFA ---
@router.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    tarefa = task_service.buscar_tarefa(id)
    if not tarefa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Tarefa não encontrada"
            )
    return tarefa

# --- CRIAR TAREFA ---
@router.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(task: TaskCreate):

    return task_service.criar_tarefa(task)

# --- ATUALIZAR TAREFA ---
@router.put("/tarefas/{id}")
def atualizar_tarefa(id: int, task: TaskCreate):
    tarefa = task_service.atualizar_tarefa(id, task)
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Tarefa não encontrada"
        )
    return tarefa


        
# --- DELETAR TAREFA ---
@router.delete("/tarefas/{id}")

def deletar_tarefa(id: int):
    tarefa = task_service.deletar_tarefa(id)
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Tarefa não encontrada"
        )
    return tarefa

        
