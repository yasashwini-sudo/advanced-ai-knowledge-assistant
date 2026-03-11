from fastapi import FastAPI
from app.api.routes import router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="AI Knowledge Assistant",
    description="Backend for document based AI assistant",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Knowledge Assistant API Running"}