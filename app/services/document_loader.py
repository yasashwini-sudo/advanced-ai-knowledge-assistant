from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

import re

def clean_text(text):
    # Fix spaced letters like "M O H I T"
    text = re.sub(r'(?<=\b[A-Z])\s(?=[A-Z]\b)', '', text)

    # Fix spaced numbers like "9 1 7 6"
    text = re.sub(r'(?<=\d)\s+(?=\d)', '', text)

    # Fix spaced email symbols
    text = re.sub(r'\s*@\s*', '@', text)
    text = re.sub(r'\s*\.\s*', '.', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def load_and_split_pdf(file_path: str):

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Clean text
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)
        doc.metadata["source"] = file_path
        
    print("Splitting documents...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")
    print(chunks[0].page_content)

    return chunks