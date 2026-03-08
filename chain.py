from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .config import GROQ_API_KEY, GROQ_MODEL


llm = ChatGroq(model = GROQ_MODEL, api_key = GROQ_API_KEY, temperature = 0.2)

prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Professional AI Assistant"),
        ("human", "{input}")
      ])


parser = StrOutputParser()


chains = prompt | llm | parser

def generate_response(user_input: str) -> str:
    response = chains.invoke({"input" : user_input})
    return response

  
