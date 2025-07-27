import pandas as pd
from langchain.agents import Tool
from langchain.globals import set_debug
from langchain_core.prompts import PromptTemplate
from langchain_experimental.tools import PythonAstREPLTool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.language_models.chat_models import BaseChatModel
from typing import Type




class AgenteDataFrame:

    # Vamos utilizar injeção de dependência no construtor, para conseguimos,
    # trocar a LLM usada e o DataFrame sem ter que alterar nosso código do
    # Agente. :)
    def __init__(self, llm:Type[BaseChatModel], df:pd.DataFrame, isDebug:bool = True) -> None:
        self.__df = df
        self.__llm = llm
        set_debug(isDebug)

    # Não vamos criar do zero a ferramenta o LangChain tem várias prontas! :)
    # https://python.langchain.com/docs/integrations/tools/
    @property
    def ferramentas(self) -> None:
        """
        Adiciona uma ferramenta ao agente.
        """
        return  [
                    Tool(
                        name="Códigos Python",
                        func=PythonAstREPLTool(locals={"df": self.__df}),
                        description="""Utilize esta ferramenta sempre que o usuário solicitar cálculos, consultas ou transformações
                        específicas usando Python diretamente sobre o DataFrame `df`.
                        Exemplos de uso incluem: "Qual é a média da coluna X?", "Quais são os valores únicos da coluna Y?",
                        "Qual a correlação entre A e B?". Evite utilizar esta ferramenta para solicitações mais amplas ou descritivas,
                        como informações gerais sobre o DataFrame, resumos estatísticos completos ou geração de gráficos — nesses casos,
                        use as ferramentas apropriadas."""
                    )
                ]

    # Vamos criar o nosso prompt, baseado no ReAct (Reasoning + Acting)
    # O agente, a cada passo, faz:
    #   1. Pensamento (Thought / Reasoning): O LLM escreve o raciocínio do que está tentando fazer.
    #   2. Ação (Action): O LLM escolhe uma ferramenta e uma entrada (exemplo: chamar uma API, consultar um banco de dados,
    #      ler um PDF, fazer uma consulta SQL).
    #   3. Observação (Observation): O agente recebe a resposta da ferramenta (exemplo:
    #      "Resposta da API: 123 resultados encontrados").
    #   4. Volta ao passo 1 até chegar a uma Resposta Final (Final Answer).
    @property
    def react_prompt(self) -> str:
        """
        Define o prompt para o agente.
        """
        df_head:str = self.__df.head().to_markdown()
        return PromptTemplate(
                    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
                    partial_variables={"df_head": df_head},
                    template = """
                        Você é um assistente que sempre responde em português.

                        Você tem acesso a um dataframe pandas chamado `df`.
                        Aqui estão as primeiras linhas do DataFrame, obtidas com `df.head().to_markdown()`:

                        {df_head}

                        Responda às seguintes perguntas da melhor forma possível.

                        Para isso, você tem acesso às seguintes ferramentas:

                        {tools}

                        Use o seguinte formato:

                        Question: a pergunta de entrada que você deve responder
                        Thought: você deve sempre pensar no que fazer
                        Action: a ação a ser tomada, deve ser uma das [{tool_names}]
                        Action Input: a entrada para a ação
                        Observation: o resultado da ação
                        ... (este Thought/Action/Action Input/Observation pode se repetir N vezes)
                        Thought: Agora eu sei a resposta final
                        Final Answer: a resposta final para a pergunta de entrada original.

                        Comece!

                        Question: {input}
                        Thought: {agent_scratchpad}"""
                )

    def executar(self, question:str) -> dict[str,str]:
        """
        Executa o agente com a entrada fornecida.
        """
        try:
            agente = create_react_agent(llm=self.__llm, tools=self.ferramentas, prompt=self.react_prompt)
            executor = AgentExecutor(agent=agente, tools=self.ferramentas, handle_parsing_errors=True)
            resposta = executor.invoke({"input": question})
            return resposta
        except Exception as e:
            print(f"Erro ao executar o agente: {e}")
            return {"error": str(e)}