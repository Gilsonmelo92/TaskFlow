from pydantic import BaseModel 

class TaskCreate(BaseModel):
    titulo: str

class TaskResponse(BaseModel):
    id: int
    titulo: str
    concluida: bool

class MessageResponse(BaseModel):
    mensagem: str