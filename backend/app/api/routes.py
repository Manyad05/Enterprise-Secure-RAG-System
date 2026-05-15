from fastapi import APIRouter
from pydantic import BaseModel

from app.pipelines.rag_pipeline import run_rag

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask")
def ask_question(request: QueryRequest):

    result = run_rag(request.query)

    return result