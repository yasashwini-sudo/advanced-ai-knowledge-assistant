from langchain_community.vectorstores import FAISS
from app.services.embedding_service import get_embedding_model

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )
    vector_store.save_local("faiss_index")
    
    return vector_store