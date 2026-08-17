from app.schemas.task import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session
from app.database.models import Tarefa

# --- LISTAR TAREFAS ---
#"Use esta Session para consultar a tabela representada pelo Model Tarefa e me devolva todos os registros."

def listar_tarefas(db: Session):
    return db.query(Tarefa).all()

# --- BUSCAR TAREFA ---
def buscar_tarefa(db: Session, id: int):
    return db.query(Tarefa).filter(Tarefa.id == id).first()

# --- CRIAR TAREFA ---
def criar_tarefa(db:Session, task: TaskCreate):
    nova_tarefa = Tarefa(
        titulo=task.titulo,
        concluida=False
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    
    return nova_tarefa

# --- ATUALIZAR TAREFA ---
def atualizar_tarefa(db: Session, id: int, task: TaskUpdate):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        return None
    
    if task.titulo is not None:
        tarefa.titulo = task.titulo

    if task.concluida is not None: 
        tarefa.concluida = task.concluida


    db.commit()
    db.refresh(tarefa)

    return tarefa


        
# --- DELETAR TAREFA ---
def deletar_tarefa(db: Session,id: int):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        return None

    db.delete(tarefa)
    db.commit()

    return {
            "mensagem": "Tarefa deletada com sucesso"
            }


