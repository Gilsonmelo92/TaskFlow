from pydantic import BaseModel, Field, field_validator, ConfigDict 

class TaskCreate(BaseModel):

    model_config = ConfigDict(extra = "forbid")  # Impede campos extras no payload

#validator para garantir que o título tenha no mínimo 3 caracteres e no máximo 100 caracteres    
    titulo: str = Field(
        min_length=3, 
        max_length=100)

#validator para garantir que o título não seja vazio ou contenha apenas espaços em branco

    @field_validator("titulo", mode="before")
    @classmethod
    def validar_titulo(cls, valor):
        valor = valor.strip()  # Remove espaços em branco no início e no final

        if not valor:
            raise ValueError("O título não pode ser vazio ou conter apenas espaços em branco.")
        return valor

class TaskResponse(BaseModel):
    id: int
    titulo: str
    concluida: bool

class MessageResponse(BaseModel):
    mensagem: str