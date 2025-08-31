from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from text_from_kb import retriever, chatbot  # import retriever and LLM

def create_rag_chain():
    system_prompt = (
        "You are an intelligent assistant. Use ONLY the provided context to answer the question. "
        "If the answer is not in the context, reply: 'I don’t know based on the available information.' "
        "Answer clearly, concisely, and in a helpful manner. Avoid adding information not present in the context.\n\n"
        "Context:\n{context}\n\n"
        "Question: {question}\n\n"
        "Answer:"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(chatbot.llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qa_chain)
    return rag_chain

rag_chain = create_rag_chain()
