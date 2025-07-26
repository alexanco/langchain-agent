# 🧠 FastAPI + LangChain CSV QA API

Este projeto é uma API RESTful desenvolvida com **FastAPI** e **LangChain**, projetada para responder perguntas baseadas em dados de arquivos CSV. Ele utiliza modelos de linguagem (LLMs) para interpretar e responder perguntas, suportando múltiplos arquivos CSV e agentes inteligentes.

## ✨ Funcionalidades

- 🔍 Rota de API para envio de perguntas em linguagem natural
- 📊 Análise de dados estruturados a partir de arquivos CSV
- 🧠 Uso de agentes da LangChain com LLMs (como OpenAI)
- 🐳 Execução via Docker Compose para facilitar o deploy
- 🔐 Suporte a variáveis de ambiente para segurança e configuração

## 🗂️ Estrutura do Projeto

```
langchain-agent/
├── app/
│   ├── __init__.py
│   ├── main.py              # Instância do FastAPI e inclusão de rotas
│   ├── models/
│   │   ├── __init__.py
│   │   └── question.py      # Modelos Pydantic para entrada/saída
│   ├── routers/
│   │   ├── __init__.py
│   │   └── qa.py            # Rotas de perguntas e respostas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── agent.py         # Inicialização do agente LangChain e LLM
│   │   └── csv_loader.py    # Utilitário para carregar CSVs
|   ├── requirements.txt     # Dependências do projeto
|   ├── Dockerfile           # Dockerfile com a imagem a ser usada pelo projeto
|   ├── docker-compose.yml   # Docker compose do projeto
├── data/
│   └── csv_files/           # Armazena os CSVs que serão analisados
│       └── exemplo.csv
├── .env                     # Variáveis de ambiente (ex.: API keys)
└── README.md                # Documentação e instruções de uso
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone git@github.com:alexanco/langchain-agent.git
cd langchain-agent
```

### 2. Configure sua chave OpenAI

Crie um arquivo `.env` na raiz com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Execute com Docker Compose

```bash
docker-compose up --build
```

A aplicação estará acessível em `http://localhost:8000`.

### 4. Faça uma pergunta

Envie uma requisição `POST` para:

```http
POST /perguntas
Content-Type: application/json

{
  "pergunta": "Qual foi o total de vendas em 2024?",
  "arquivo_csv": "vendas_2024.csv"
}
```

## 📚 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Pandas](https://pandas.pydata.org/)
- [OpenAI](https://platform.openai.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## ⚠️ Aviso de Segurança

O uso de `create_pandas_dataframe_agent` utiliza um interpretador Python REPL, o que pode representar risco de execução arbitrária de código. É fortemente recomendado isolar o ambiente de execução, validar perguntas e arquivos, e considerar abordagens baseadas em SQL para produção segura.

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.

## 🙋 Contribuições

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.
