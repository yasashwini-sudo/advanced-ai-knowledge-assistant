from fastapi import APIRouter, UploadFile, File
import shutil
import os
from pydantic import BaseModel

from app.services.document_loader import load_and_split_pdf
from app.services.vector_store import create_vector_store
from app.services.rag_pipeline import create_qa_chain

router = APIRouter()

vector_db = None
qa_chain = None


class QuestionRequest(BaseModel):
    question: str


@router.get("/health")
def health_check():
    return {"status": "running"}


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):

    global vector_db
    global qa_chain

    os.makedirs("data", exist_ok=True)

    file_location = f"data/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = load_and_split_pdf(file_location)

    vector_db = create_vector_store(chunks)

    qa_chain = create_qa_chain(vector_db)

    return {
        "filename": file.filename,
        "chunks_created": len(chunks),
        "status": "Document indexed successfully"
    }


@router.post("/ask")
def ask_question(request: QuestionRequest):

    global qa_chain

    if qa_chain is None:
        return {"error": "Upload a document first"}

    response = qa_chain.invoke({"query": request.question})

    return {
        "question": request.question,
        "answer": response["result"]
    }