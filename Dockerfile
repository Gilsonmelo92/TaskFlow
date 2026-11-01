# Imagem base com Python
FROM python:3.13-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Caminho do banco SQLite dentro do container
ENV DATABASE_URL=sqlite:////data/database.db

# Copia a lista de dependências
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app/ ./app/

# Documenta a porta usada pela API
EXPOSE 8000

# Inicia a API FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
