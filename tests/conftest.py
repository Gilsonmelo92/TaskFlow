import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.database import Base, get_db
from app.database.models import Tarefa
from fastapi.testclient import TestClient
from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_database.db"

engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)


#fábrica de sessões exclusiva dos nossos testes
TestingSessionLocal = sessionmaker(
    bind=engine_test,
    autocommit= False,
    autoflush= False #Evita que o SQLAlchemy envie automaticamente alterações pendentes ao banco antes de determinadas operações.
)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine_test) # Cria no banco de testes todas as tabelas registradas no Base
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close() 
        Base.metadata.drop_all(bind=engine_test) # Cria no banco de testes todas as tabelas registradas no Base
  
@pytest.fixture
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)

    yield client

    app.dependency_overrides.clear()