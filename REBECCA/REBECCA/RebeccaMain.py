from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
import json
from ApiKey import api

#Variaveis Globais Uteis
apikey = api
userMSG = ""


#Funções

def resposta(mensagem):
    saida=llm.invoke([
        SystemMessage(content=memoria),
        HumanMessage(content=mensagem)
    ])
    a = f'User{mensagem}'
    with open("memoria.json","a") as arquivo:
        arquivo.write("\n{"+a+"}")
        print("memoria atualizada")
    return saida.model_dump()

def lerMem():
    with open("memoria.json","r") as arquivo:
       return arquivo.read()

#Configurando o Agente Principal
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.6,
        api_key=api
    )
except Exception as error:
    print(error)

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.6,
        api_key=api
    )
except Exception as error:
    print(error)


#Executando tudo

while True:
    memoria = lerMem()
    userMSG = input("Voce:")
    try:
        print(f"Rebecca:{resposta(userMSG)["content"]}")
    except Exception as error:
        print(error)