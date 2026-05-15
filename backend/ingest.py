from app.loaders.pdf_loader import load_text_file
from app.vectordb.chroma_store import create_vector_store

documents = load_text_file(
    "../datasets/pdfs/hr_policy.txt"
)

create_vector_store(documents)

print("Documents embedded successfully")