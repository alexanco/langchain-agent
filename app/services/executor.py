import os
import pandas as pd
from services.agent_dataframe import AgenteDataFrame
from dotenv import load_dotenv

# Cria a llm e recupera o token do secrets
from langchain_groq import ChatGroq

class Executor:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Executor, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            
            # Caminho para o arquivo CSV no container
            csv_path = "data/csv_files/Placement_Data_Full_Class.csv"

            # Verifica se o arquivo existe
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"Arquivo CSV não encontrado: {csv_path}")
            
            self.__df = pd.read_csv(filepath_or_buffer=csv_path)

            load_dotenv()

            self.__API_KEY = os.getenv("GROQ_API_KEY")
            self.__llm = ChatGroq(temperature=0, groq_api_key=self.__API_KEY, model_name='llama3-70b-8192')
            self.__agent_df = AgenteDataFrame(llm=self.__llm, df=self.__df)
            
            Executor._initialized = True
    
    
    def executar(self, question: str) -> dict[str, str]:
        """
        Executa a pergunta no agente e retorna a resposta.
        """
        resposta = self.__agent_df.executar(question)
        return {"output": resposta['output']}