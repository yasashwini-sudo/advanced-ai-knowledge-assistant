from fastapi import APIRouter, UploadFile, File
import shutil
from pydantic import BaseModel

from app.services.document_loader import load_and_split_pdf
from app.services.vector_store import create_vector_store
from app.services.rag_pipeline import create_qa_chain

uploaded_documents = []
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

    file_location = f"data/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    uploaded_documents.append(file.filename)

    chunks = load_and_split_pdf(file_location)

    vector_db = create_vector_store(chunks)

    # create QA chain after vector DB is ready
    qa_chain = create_qa_chain(vector_db)

    return {"message": "Document uploaded successfully"}


@router.post("/ask")
def ask_question(request: QuestionRequest):

    global qa_chain

    if qa_chain is None:
        return {"error": "Upload a document first"}

    response = qa_chain.invoke({"query": request.question})

    sources = []
    for doc in response["source_documents"]:
        sources.append(doc.metadata.get("source", "Unknown"))

    return {
        "question": request.question,
        "answer": response["result"],
        "sources": list(set(sources))
    }

@router.get("/documents")
def list_documents():
    return {
        "documents": uploaded_documents
    }

import os

@router.delete("/documents/{filename}")
def delete_document(filename: str):

    file_path = f"data/{filename}"

    if os.path.exists(file_path):
        os.remove(file_path)

    if filename in uploaded_documents:
        uploaded_documents.remove(filename)

    return {
        "message": f"{filename} deleted successfully"
    }