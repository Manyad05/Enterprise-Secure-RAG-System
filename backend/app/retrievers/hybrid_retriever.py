from langchain_community.vectorstores import Chroma

from app.embeddings.embedding_model import (
    get_embedding_model
)

def retrieve_documents(query):

    embeddings = get_embedding_model()

    vectordb = Chroma(
        persist_directory="chroma_storage",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever()

    docs = retriever.invoke(query)

    return docs