from langchain_community.vectorstores import Chroma
from app.embeddings.embedding_model import get_embedding_model

def create_vector_store(documents):

    embeddings = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="chroma_storage"
    )

    vectordb.persist()

    return vectordb