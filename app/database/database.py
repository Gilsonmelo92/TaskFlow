from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#Criação do banco de dados SQLite
engine = create_engine("sqlite:///app/database/database.db",  
connect_args={"check_same_thread": False})

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