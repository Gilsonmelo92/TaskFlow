from fastapi import FastAPI
from app.routers.tasks import router as tasks_router

app = FastAPI(
    title = "TaskFlow API",
    version = "0.1.0"
)

app.include_router(tasks_router)


@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao TaskFlow!"}