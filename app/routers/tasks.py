from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskResponse, MessageResponse, TaskUpdate
from app.database.database import get_db
from app.services import task_service


router = APIRouter()

# --- LISTAR TAREFAS ---
@router.get(
        "/tarefas", 
        response_model=list[TaskResponse]
        )
def listar_tarefas(
    db: Session = Depends(get_db)
    ):
    return task_service.listar_tarefas(db)


# --- BUSCAR TAREFA ---
@router.get(
        "/tarefas/{id}", 
        response_model=TaskResponse
        )
def buscar_tarefa(
    id: int, 
    db: Session = Depends(get_db)
    ):
    
    tarefa = task_service.buscar_tarefa(db, id)

    if not tarefa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "Tarefa não encontrada"
            )
    return tarefa

# --- CRIAR TAREFA ---
@router.post(
        "/tarefas", 
        response_model=TaskResponse, 
        status_code=status.HTTP_201_CREATED
        )
def criar_tarefa(
    task: TaskCreate,
    db: Session = Depends(get_db)
    ):
    return task_service.criar_tarefa(db, task)

# --- ATUALIZAR TAREFA ---
@router.put(
        "/tarefas/{id}", 
        response_model=TaskResponse
        )
def atualizar_tarefa(
     id: int, 
     task: TaskUpdate, 
     db: Session = Depends(get_db)
    ):

    tarefa = task_service.atualizar_tarefa(db, id, task)

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Tarefa não encontrada"
        )
    return tarefa


        
# --- DELETAR TAREFA ---
@router.delete(
        "/tarefas/{id}", response_model=MessageResponse
        )
def deletar_tarefa(
     id: int, 
     db: Session = Depends(get_db)
):

    tarefa = task_service.deletar_tarefa(db, id)

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Tarefa não encontrada"
        )
    return tarefa

        
