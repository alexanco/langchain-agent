from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import qa

app = FastAPI(
    title="API de Perguntas com LangChain e CSVs",
    description="Permite enviar perguntas e obter respostas baseadas em dados CSV via LangChain",
    version="0.1.0",
)

# Configuração de CORS (opcional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão da rota de perguntas
app.include_router(qa.router, prefix="/questions", tags=["questions"])
