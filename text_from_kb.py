from file_loader import *
import os
from langchain_chroma import Chroma
from chatbot import ChatbotModel
from text_from_kb import*
from langchain.text_splitter import RecursiveCharacterTextSplitter


## replace your knowledge base folder path here
KNOWLEDGE_BASE_DIR = r"C:\Users\Sai charan\Desktop\end_to_end_breast_cancer_project\knowledgebase-multi-file-chatbot\knowledge_base"

def load_knowledge_base():
    all_docs = []
    for file_name in os.listdir(KNOWLEDGE_BASE_DIR):
        file_path = os.path.join(KNOWLEDGE_BASE_DIR, file_name)
        
        if os.path.isfile(file_path):
            try:
                content = load_file(file_path)

                if isinstance(content, list):
                    content = "\n".join([str(item) for item in content])

                all_docs.append({
                    "file_name": file_name,
                    "content": content
                })
                print(f"Loaded: {file_name}")

            except Exception as e:
                print(f"Error loading {file_name}: {e}")
                continue
    return all_docs

knowledge_base = load_knowledge_base()

documents = [doc['content'] for doc in knowledge_base]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)


chunked_documents = text_splitter.create_documents(documents)

chatbot = ChatbotModel()

vectordb = Chroma.from_documents(chunked_documents, embedding=chatbot.embeddings, persist_directory="chroma_db")

retriever = vectordb.as_retriever(search_kwargs={"k": 3})


