from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


#Criação do banco de dados SQLite

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///app/database/database.db"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# CRIAR uma sessão para interagir com o banco de dados
SessionLocal = sessionmaker(bind=engine)

#Será utilizada por todos os Models.
Base = declarative_base()

def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()