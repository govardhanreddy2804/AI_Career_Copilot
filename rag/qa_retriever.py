# rag/qa_retriever.py
from langchain.chains import RetrievalQA

def create_qa_chain(vectorstore, llm):
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
