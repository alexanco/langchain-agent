from fastapi import APIRouter, HTTPException
from models.question import QuestionRequest
from services.agent_executor import AgentExecutor

router = APIRouter()

@router.post("/", summary="Enviar pergunta e receber resposta")
async def ask_question(request: QuestionRequest) -> dict:
    """Recebe uma pergunta do usuário e retorna a resposta baseada nos CSVs."""
    if not request.question:
        raise HTTPException(status_code=400, detail="Pergunta não pode ser vazia")

    # Inicializa (ou reutiliza) o agente
    agentExecutor = AgentExecutor()

    # Use o agente para gerar a resposta. O método `invoke` aceita um dicionário
    # com a chave "input" para o agente do LangChain.
    try:
        result = agentExecutor.execute(request.question)
    except Exception as e:
        # Trate exceções específicas se desejar
        raise HTTPException(status_code=500, detail=str(e))

    # Retorne a resposta no formato desejado
    return {"answer": result['output']}
