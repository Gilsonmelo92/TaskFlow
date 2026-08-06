from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100))
    concluida = Column(Boolean)



