# chatbot.py
import os
from dotenv import load_dotenv, find_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOllama

from text_from_kb import*

class ChatbotModel:
    def __init__(self):
        """Initialize the chatbot models"""
        # Load environment variables
        load_dotenv(find_dotenv())
        self.api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

        if not self.api_token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")

        self.llm = None
        self.embeddings = None

        self.setup_models()

    def setup_models(self):
        try:
            # Initialize LLM
            self.llm = ChatOpenAI(
                temperature=0.0,
                model="openai/gpt-oss-120b",
                base_url="https://router.huggingface.co/v1",
                api_key=self.api_token,
            )
            # self.llm = ChatOllama(model="mistral")

            # Initialize HuggingFace embeddings
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-mpnet-base-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )

            print("Chatbot models initialized successfully.")

        except Exception as e:
            print(f"Error initializing models: {e}")
            raise
        
# # knowledge_base = load_knowledge_base()

# # Flatten texts for embeddings
# documents = [doc['content'] for doc in knowledge_base]

# # Create embeddings & vector DB using your chatbot
# # from langchain_chroma import Chroma
# # from chatbot import ChatbotModel

# chatbot = ChatbotModel()
# vectordb = Chroma.from_texts(documents, embedding=chatbot.embeddings, persist_directory="chroma_db")

