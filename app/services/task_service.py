from app.schemas.task import TaskCreate


tarefas = []

# --- LISTAR TAREFAS ---
def listar_tarefas():
    return tarefas

# --- BUSCAR TAREFA ---
def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

#    com o importe do HTTPException, podemos retornar um erro 404 caso a tarefa não seja encontrada.


# --- CRIAR TAREFA ---
def criar_tarefa(task: TaskCreate):
    #Gera um novo ID baseado no maior ID existente.
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": task.titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    return nova_tarefa

# --- ATUALIZAR TAREFA ---
def atualizar_tarefa(id: int, task: TaskCreate):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = task.titulo
            return tarefa


        
# --- DELETAR TAREFA ---
def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return {
                "mensagem": "Tarefa deletada com sucesso"
            }


