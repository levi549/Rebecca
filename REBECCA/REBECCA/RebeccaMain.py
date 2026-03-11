from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
import edge_tts
import asyncio
import os
from playsound import playsound
import json
from ApiKey import api
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import sys
import platform
from pathlib import Path

#Variaveis Globais Uteis
apikey = api
userMSG = ""
voz = "pt-BR-FranciscaNeural"
Rate = "+3%"
voicefile = "RebeccaVoice.mp3"
q = queue.Queue()

try:
    model = Model("ModelSTT/vosk-model-small-pt-0.3")
except Exception as e:
    print(e)

STT = KaldiRecognizer(model, 16000)

#Funções
def limparterm():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def restart():
    sys.stdout.flush()
    sys.stderr.flush()
    os.execv(sys.executable, ['python'] + sys.argv)

def callback(indata, frames, time, status):
    q.put(bytes(indata))
    print(status)

async def texttospeech(text):
    if os.path.exists(voicefile):
        try:
            os.remove(voicefile)
        except:
            await asyncio.sleep(0.5)
            os.remove(voicefile)
    tts = edge_tts.Communicate(text,voz,rate=Rate)
    await tts.save(voicefile)
    print("arquivo de voz salvo")
    playsound(voicefile)

def resposta(mensagem):
    docs = retriever.invoke(mensagem)
    contexto = "\n\n".join(d.page_content for d in docs) if docs else ""
    saida = llm.invoke([
        SystemMessage(content=memoria + "\n\n## Contexto FETEPS:\n" + contexto),
        HumanMessage(content=mensagem)
    ])
    return saida.model_dump()

def lerMem():
    with open("memoria.json","r") as arquivo:
       return arquivo.read()

# Configurando o RAG
try:
    infos= Path("content/FETEPS.pdf")
    loader = PyMuPDFLoader(str(infos))
    pdf = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(pdf)
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(search_type="similarity_score_threshold",
                                        search_kwargs={"score_threshold":0.3, "k": 4})
except Exception as e:
    limparterm()
    print(e)
    restart()



#Configurando o Agente Principal
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.6,
        api_key=api
    )
except Exception as error:
    print(error)


#Executando tudo

try:
    with sd.RawInputStream(
    samplerate=16000,
    blocksize=32000,
    dtype="int16",
    channels=1,
    callback=callback
    ):
        
        while True:
            data = q.get()
            if STT.AcceptWaveform(data):
                #print(STT.PartialResult()["text"])
                userMSG = json.loads(STT.Result())["text"]
                print(userMSG)
                if "rebeca" in userMSG:
                    memoria = lerMem()
                    resposText = resposta(userMSG)["content"]
                    try:
                        print(f"Rebecca:{resposText}")
                        asyncio.run(texttospeech(resposText))
            
                    except Exception as error:
                        print(error)
            else:
                partial = json.loads(STT.PartialResult())
                print(partial["partial"])
except Exception as e:
    print(e)