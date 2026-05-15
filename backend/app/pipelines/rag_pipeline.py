from app.retrievers.hybrid_retriever import retrieve_documents

def run_rag(query):

    docs = retrieve_documents(query)

    results = []

    for doc in docs:

        results.append({
            "content": doc.page_content,
            "metadata": doc.metadata
        })

    return {
        "query": query,
        "results": results
    }