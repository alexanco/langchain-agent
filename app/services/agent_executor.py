import os
import pandas as pd
from services.agent_dataframe import AgentDataFrame
from dotenv import load_dotenv

# Cria a llm e recupera o token do secrets
from langchain_groq import ChatGroq

class AgentExecutor:
    _instance      = None
    _initialized   = False
    _csv_file      = ""

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AgentExecutor, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            
            load_dotenv()

            self.__API_KEY = os.getenv("GROQ_API_KEY")
            self.__llm = ChatGroq(temperature=0, groq_api_key=self.__API_KEY, model_name='llama3-70b-8192')

            AgentExecutor._initialized = True


    def execute(self, question: str, csv_file: str) -> dict[str, str]:
        """
        Executa a pergunta no agente e retorna a resposta.
        """

        if not csv_file:
            raise ValueError("O arquivo CSV não pode ser vazio")
        
        # Atualiza o caminho do CSV se necessário
        if csv_file != self._csv_file:
            csv_path = f"data/csv_files/{csv_file}"
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"Arquivo CSV não encontrado: {csv_file}")
            
            self.__df = pd.read_csv(filepath_or_buffer=csv_path)
            self.__agent_df = AgentDataFrame(llm=self.__llm, df=self.__df, isDebug=False)

        response = self.__agent_df.execute(question)
        return {"output": response['output']}