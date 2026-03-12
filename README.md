# Advanced AI Knowledge Assistant (RAG Based)

## Overview

The **Advanced AI Knowledge Assistant** is a Retrieval Augmented Generation (RAG) based application designed to allow users to upload documents and interact with them using natural language questions.

Traditional Large Language Models generate answers based only on their pre-trained knowledge, which can lead to outdated or inaccurate responses. This project addresses that limitation by integrating a **Retrieval Augmented Generation (RAG) pipeline** that retrieves relevant information from user-provided documents before generating answers.

By combining **document retrieval, embeddings, vector search, and language models**, the system produces responses that are grounded in the actual content of the uploaded documents.

The application is implemented as a **FastAPI backend service** and provides endpoints for uploading documents and querying the knowledge base.

---

## Problem Statement

Large Language Models are powerful but have two major limitations:

1. They do not have access to private or domain-specific documents.
2. They may hallucinate answers when they lack context.

To solve this, the system introduces a **Retrieval Augmented Generation architecture**, which retrieves relevant information from a document knowledge base and feeds it into the language model to generate accurate answers.

---

## Key Features

* Upload and process PDF documents
* Automatic document parsing and chunking
* Embedding generation for semantic understanding
* Vector database storage for efficient retrieval
* Context-aware question answering
* Retrieval Augmented Generation pipeline
* FastAPI backend with REST API endpoints
* Scalable architecture for future extensions

---

## System Architecture

The system follows a **RAG (Retrieval Augmented Generation) pipeline** consisting of multiple stages:

### 1. Document Ingestion

The user uploads a PDF document through the API.

### 2. Document Processing

The uploaded document is loaded and split into smaller text chunks. Chunking ensures that the retrieval process works efficiently and that the language model receives manageable context.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector representation using embedding models. These embeddings capture the semantic meaning of the text.

### 4. Vector Storage

The embeddings are stored in a **vector database (FAISS)** which enables fast similarity searches.

### 5. Query Processing

When a user asks a question:

1. The question is converted into an embedding
2. The vector database searches for the most relevant document chunks
3. The retrieved chunks are passed to the language model as context
4. The model generates a response based on the retrieved knowledge

This ensures the answers are **grounded in the document content**.

---

## Technology Stack

### Backend Framework

* FastAPI

### Programming Language

* Python

### AI Framework

* LangChain

### Embeddings Model

* HuggingFace Embeddings

### Vector Database

* FAISS (Facebook AI Similarity Search)

### Server

* Uvicorn

### Data Validation

* Pydantic

---

## Project Structure

```
advanced-ai-knowledge-assistant
│
├── app
│   ├── main.py
│   ├── routes
│   │   └── routes.py
│   │
│   └── services
│       ├── document_loader.py
│       ├── embedding_service.py
│       ├── rag_pipeline.py
│       └── vector_store.py
│
├── uploaded_docs
│
├── requirements.txt
└── README.md
```

### Description of Important Modules

**main.py**
Initializes the FastAPI application and includes API routes.

**routes.py**
Defines API endpoints for uploading documents and asking questions.

**document_loader.py**
Handles loading PDF files and splitting them into smaller text chunks.

**embedding_service.py**
Generates embeddings for document chunks using HuggingFace embedding models.

**vector_store.py**
Creates and manages the FAISS vector database.

**rag_pipeline.py**
Builds the Retrieval Augmented Generation chain that connects retrieval with the language model.

---

## Installation

Clone the repository:

```
git clone https://github.com/yasashwini-sudo/advanced-ai-knowledge-assistant
```

Navigate to the project directory:

```
cd advanced-ai-knowledge-assistant
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the virtual environment:

Windows:

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server using:

```
uvicorn app.main:app --reload
```

Once the server starts, open the API documentation:

```
http://127.0.0.1:8000/docs
```

The interactive documentation allows testing the API endpoints directly.

---

## API Endpoints

### Upload Document

Uploads a PDF document and processes it into the vector database.

Endpoint:

```
POST /upload
```

Functionality:

* Accepts a PDF file
* Loads the document
* Splits text into chunks
* Generates embeddings
* Stores vectors in FAISS database

---

### Ask Question

Allows users to ask questions related to the uploaded documents.

Endpoint:

```
POST /ask
```

Functionality:

* Accepts a question
* Retrieves relevant document chunks
* Passes context to the language model
* Generates an answer based on retrieved information

---

## Example Workflow

1. Upload a document using the `/upload` endpoint.
2. The system processes the document and stores embeddings in the vector database.
3. Ask a question using the `/ask` endpoint.
4. The system retrieves relevant document chunks.
5. The language model generates a response using the retrieved context.

---

## Advantages of the RAG Approach

* Reduces hallucinations in AI responses
* Enables domain-specific knowledge integration
* Allows real-time document understanding
* Scales easily with additional documents
* Improves response accuracy

---

## Future Improvements

The system can be extended with several enhancements:

* Multi-document support
* Support for additional file formats (DOCX, TXT)
* Frontend interface for user interaction
* Integration with advanced vector databases like Pinecone or Weaviate
* Authentication and user management
* Deployment using Docker and cloud platforms
* Improved retrieval strategies

---

## Author

**Yasaswini**

Computer Science Student

---

## License

This project is developed for educational and research purposes.
