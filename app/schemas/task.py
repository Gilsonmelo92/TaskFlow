from pydantic import BaseModel 

class TaskCreate(BaseModel):
    titulo: str
