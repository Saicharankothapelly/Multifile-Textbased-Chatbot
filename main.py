# main.py
from rag_chain import rag_chain

def chat():
    print("PDF/KB Chatbot is ready! Type 'exit' to quit.")
    while True:
        question = input("\nYou: ")
        if question.lower() == "exit":
            break
        result = rag_chain.invoke({"input": question})
        print("\nBot:", result["answer"])

if __name__ == "__main__":
    chat()
