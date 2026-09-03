from fastapi import FastAPI
from app.routers.tasks import router as tasks_router
from app.database.database import Base, engine
from app.database import models

app = FastAPI(
    title ="TaskFlow API",
    description= "API REST para gerenciamento de tarefas.",
    version ="0.1.0"
)

app.include_router(tasks_router)


@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao TaskFlow!"}

Base.metadata.create_all(bind=engine)  