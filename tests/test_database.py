from app.database.models import Tarefa
from app.database.database import Base


def test_database_connection(db):
    assert db is not None

def test_create_task(db):
    tarefa = Tarefa(
        titulo="Estudar testes com pytest",
        concluida=False
    )
    #colocar o objeto na session
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa) #atualiza o objeto Python com os dados que estão no banco.

    assert tarefa.id is not None
    assert tarefa.titulo == "Estudar testes com pytest"
    assert tarefa.concluida is False

# Teste para verificar se o banco está realmente vazio. 
def test_database_starts_empty(db):
    tarefas = db.query(Tarefa).all()

    assert tarefas ==[]
