from langchain_community.vectorstores import Chroma
from app.services.embedding_service import get_embedding_model

VECTOR_DB_PATH = "chroma_db"


def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    vector_store.add_documents(chunks)

    vector_store.persist()

    return vector_store


def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    return vector_store