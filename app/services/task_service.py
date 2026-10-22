from app.schemas.task import TaskCreate, TaskUpdate
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from app.database.models import Tarefa

# --- LISTAR TAREFAS ---
#"Use esta Session para consultar a tabela representada pelo Model Tarefa e me devolva todos os registros."


def listar_tarefas(
    db: Session,
    page: int = 1,
    limit: int = 10,
    concluida: bool | None = None,
    ordenar_por: str = "id",
    ordem: str = "asc",
):
    offset = (page - 1) * limit

    # 1. Criar a query inicial
    query = db.query(Tarefa)

    # 2. Aplicar o filtro, se informado
    if concluida is not None:
        query = query.filter(Tarefa.concluida == concluida)

    # 3. Contar os resultados após o filtro
    total = query.count()

    # 4. Definir os campos permitidos para ordenação
    campos_ordenacao = {
        "id": Tarefa.id,
        "titulo": Tarefa.titulo,
        "concluida": Tarefa.concluida,
    }

    # 5. Validar o campo de ordenação
    if ordenar_por not in campos_ordenacao:
        raise ValueError("Campo de ordenação inválido.")

    campo = campos_ordenacao[ordenar_por]

    # 6. Aplicar a direção da ordenação
    if ordem == "asc":
        query = query.order_by(asc(campo), asc(Tarefa.id))
    elif ordem == "desc":
        query = query.order_by(desc(campo), desc(Tarefa.id))
    else:
        raise ValueError("Ordem de ordenação inválida.")

    # 7. Aplicar a paginação
    tarefas = query.offset(offset).limit(limit).all()

    # 8. Calcular o total de páginas
    total_paginas = (total + limit - 1) // limit

    return {
        "tarefas": tarefas,
        "total": total,
        "total_paginas": total_paginas,
    }

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


