from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import jogos  # Importa o arquivo jogos.py diretamente da mesma pasta

app = FastAPI(
    title="API Série C - Live Goal",
    description="API para rastreamento de partidas da Série C do Campeonato Brasileiro",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API da Série C do Brasileirão online!", "status": "ativo"}

app.include_router(jogos.router)