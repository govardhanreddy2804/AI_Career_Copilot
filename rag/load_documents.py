# rag/load_documents.py
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def create_vectorstore(doc_paths, persist_dir="chroma_db"):
    docs = []
    for path in doc_paths:
        loader = PyPDFLoader(path) if path.endswith(".pdf") else TextLoader(path)
        docs.extend(loader.load())

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb
