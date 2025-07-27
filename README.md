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
|   ├── data/
│   |    └── csv_files/      # Armazena os CSVs que serão analisados
│   |       └── exemplo.csv
|   ├── .env                 # Variáveis de ambiente (ex.: API keys)
└── .gitignore               # git ignore do projeto
└── README.md                # Documentação e instruções de uso
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone git@github.com:alexanco/langchain-agent.git
cd langchain-agent
```

### 2. Crie uma chave de API

Para realizar os testes de forma gratuita, utilizou-se uma API Key fornecida pela Groq.
Até o momento da elaboração deste material, a Groq oferece chaves de API gratuitas para que desenvolvedores possam testar diversos modelos disponíveis.
Para obter uma API Key, basta se registrar na plataforma da Groq e gerar uma chave gratuita em sua conta.

### 3. Configure sua chave Groq

Crie um arquivo `.env` na pasta app com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Baixando o dataset
```
cd app/data/csv_files
wget https://middleware.datah.ai/Placement_Data_Full_Class.csv
```

### 5. Execute com Docker Compose

```bash
cd app
docker-compose up --build
```

- A aplicação estará acessível em `http://localhost:8000`.
- A aplicação estará acessível em `http://localhost:8000/doc`. 

### 6. Faça uma pergunta

Envie uma requisição `POST` para:

```http
POST /perguntas
Content-Type: application/json

{
  "question": "Qual é a média da coluna 'ssc_p' pela coluna 'gender'?",
  "csv_file": "Placement_Data_Full_Class.csv"
}

Response body
{
  "answer": "A média da coluna 'ssc_p' pela coluna 'gender' é 68.31 para o gênero feminino e 66.75 para o gênero masculino."
}
```


## CSV utilizado no exemplo
Fonte: https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement

Ele contém registros de estudantes de um campus (em um contexto indiano/business school), com foco em identificar fatores que influenciam se o estudante foi ou não colocado (empregado em estágio/emprego) no mercado de trabalho.

Inclui tanto aspectos acadêmicos (notas no ensino médio e superior) quanto de empregabilidade (especialização, experiência, salário oferecido).



Nome das colunas e descrições

`sl_no`: Este é um número de identificação único para cada candidato no dataset. Pense nele como um ID de registro.

`ender`: Indica o gênero do candidato. 'M' representa Masculino e 'F' representa Feminino.

`ssc_p`: Refere-se à porcentagem de notas do Ensino Médio (10ª série) do candidato. É a nota que o aluno tirou no que seria o equivalente ao fundamental II no Brasil, ou seja, 10º ano do ensino médio (ensino médio no Brasil tem 3 anos e nos EUA tem 4 anos).

`ssc_b`: Indica a instituição ou conselho educacional onde o candidato completou seu Ensino Médio (10ª série). Pode ser "Central" (referindo-se a um conselho educacional centralizado, como o CBSE na Índia) ou "Others" (outros conselhos ou instituições).

`hsc_p`: Representa a porcentagem de notas do Ensino Superior (12ª série) do candidato. É a nota que o aluno tirou no que seria o equivalente ao último ano do ensino médio no Brasil.

`hsc_b`: Informa a instituição ou conselho educacional onde o candidato concluiu seu Ensino Superior (12ª série). Similar ao ssc_b, pode ser "Central" ou "Others".

`hsc_s`: Descreve a área de especialização do candidato no Ensino Superior (12ª série). Por exemplo, "Science" (Ciências), "Commerce" (Comércio) ou "Arts" (Artes).

`degree_p`: Corresponde à porcentagem de notas do candidato na sua graduação.

`degree_t`: Indica o tipo de graduação ou campo de estudo do candidato. Por exemplo, "Comm&Mgmt" (Comércio e Gestão) ou "Sci&Tech" (Ciência e Tecnologia).

`workex`: Mostra se o candidato possui experiência de trabalho prévia. "Yes" (Sim) significa que ele tem experiência, e "No" (Não) indica que não tem.

`etest_p`: Nota em teste de aptidão (em percentagem)

`specialisation`: Especialização no MBA (Mkt&HR ou Mkt&Fin)

`mba_p`: Percentual no MBA

`status`: Se foi colocado ou não (Placed, Not Placed)

`salary`: Salário mensal oferecido (zero ou vazio se não colocado)



## 📚 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Pandas](https://pandas.pydata.org/)
- [OpenAI](https://platform.openai.com/)
- [Groq](https://groq.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## ⚠️ Aviso de Segurança

O uso de Python REPL pode representar risco de execução arbitrária de código. É fortemente recomendado isolar o ambiente de execução, validar perguntas e arquivos, e considerar abordagens baseadas em SQL para produção segura.

### PythonREPLTool

- Executa código Python diretamente
- Usa exec() e eval()
- Risco alto, pois o código arbitrário pode ser perigoso


### PythonAstREPLTool (Ast - Abstract Syntax Tree)

- Executa código com parsing seguro via ast.
- Usa análise da árvore sintática para restringir o código permitido.
- Mais seguro, pois impede execução de código perigoso

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.

## 🙋 Contribuições

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.
