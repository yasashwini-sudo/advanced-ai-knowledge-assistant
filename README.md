# Advanced AI Knowledge Assistant (RAG-Based)

## Overview

The **Advanced AI Knowledge Assistant** is a backend system that enables users to upload documents and interact with them using natural language queries.
The application uses a **Retrieval Augmented Generation (RAG)** architecture to ensure that answers are grounded in the uploaded documents instead of relying solely on a language model’s pre-trained knowledge.

Traditional Large Language Models may generate responses based only on their training data, which can result in outdated or hallucinated answers. This project solves that problem by retrieving relevant information from user-provided documents and supplying that context to the language model before generating a response.

The system is implemented as a **FastAPI-based backend service** and provides APIs for document ingestion, semantic retrieval, conversational querying, and document management.

---

## Problem Statement

Large Language Models have several limitations when used independently:

1. They do not have access to private or organization-specific documents.
2. They may generate hallucinated responses when lacking relevant context.
3. They cannot dynamically incorporate newly uploaded knowledge.

To address these issues, this project implements a **Retrieval Augmented Generation pipeline** that retrieves relevant content from uploaded documents and provides that context to the language model before generating an answer.

---

## Key Features

* Upload and process PDF documents
* Multi-document knowledge base
* Automatic document parsing and text chunking
* Embedding generation for semantic understanding
* Persistent vector database storage using Chroma
* Semantic document retrieval
* Context-grounded AI responses
* Source citation in responses
* Conversation memory for follow-up questions
* Document management APIs (list and delete documents)
* FastAPI REST API backend
* Scalable modular architecture

---

## System Architecture

The application follows a **Retrieval Augmented Generation (RAG) architecture**, which combines document retrieval with language model generation.

### 1. Document Ingestion

Users upload documents through the `/upload` API endpoint.
The documents are saved locally and prepared for processing.

### 2. Document Processing

Uploaded documents are loaded and split into smaller text chunks.
Chunking improves retrieval accuracy and ensures that the language model receives manageable context sizes.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector representation using embedding models.
These embeddings capture the semantic meaning of the text.

### 4. Vector Storage

Embeddings are stored in a **Chroma vector database**, enabling fast semantic similarity searches.

### 5. Query Processing

When a user asks a question:

1. The question is converted into an embedding.
2. The vector database retrieves the most relevant document chunks.
3. The retrieved chunks are passed to the language model as context.
4. The language model generates a response grounded in the retrieved information.

### 6. Source Attribution

The system also returns the **source documents** from which the answer was derived, increasing transparency and reliability.

### 7. Conversation Memory

The assistant maintains short-term conversational memory so that follow-up questions can reference previous responses.

Example:

User: What is the purpose of the document?
Assistant: Explains the purpose.

User: Explain it simply.
Assistant: Provides a simplified explanation based on previous context.

---

## Technology Stack

### Backend Framework

* FastAPI

### Programming Language

* Python

### AI Framework

* LangChain

### Language Model

* OpenAI GPT models

### Embeddings

* OpenAI Embedding Models

### Vector Database

* Chroma (persistent vector database)

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
│   │
│   ├── api
│   │   └── routes.py
│   │
│   └── services
│       ├── document_loader.py
│       ├── embedding_service.py
│       ├── vector_store.py
│       └── rag_pipeline.py
│
├── data
│   └── uploaded documents
│
├── chroma_db
│   └── vector database storage
│
├── requirements.txt
└── README.md
```

### Description of Important Modules

**main.py**
Initializes the FastAPI application and registers API routes.

**routes.py**
Defines API endpoints for document upload, querying the knowledge base, and document management.

**document_loader.py**
Handles loading PDF files and splitting them into smaller text chunks.

**embedding_service.py**
Generates embeddings for document chunks using OpenAI embedding models.

**vector_store.py**
Creates and manages the Chroma vector database used for semantic search.

**rag_pipeline.py**
Builds the Retrieval Augmented Generation pipeline connecting the retriever and the language model.

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

Activate the virtual environment.

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

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Once the server starts, open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

The documentation allows direct testing of all API endpoints.

---

## API Endpoints

### Upload Documents

Uploads one or more PDF documents and processes them into the knowledge base.

Endpoint:

```
POST /upload
```

Functionality:

* Accepts PDF files
* Loads documents
* Splits text into chunks
* Generates embeddings
* Stores vectors in the Chroma database

---

### Ask Question

Allows users to ask questions related to the uploaded documents.

Endpoint:

```
POST /ask
```

Functionality:

* Accepts a user query
* Retrieves relevant document chunks
* Generates a grounded AI response
* Returns answer along with source documents

---

### List Documents

Lists all uploaded documents stored in the system.

Endpoint:

```
GET /documents
```

---

### Delete Document

Deletes a specific document from the system.

Endpoint:

```
DELETE /documents/{filename}
```

---

## Example Workflow

1. Upload one or more documents using the `/upload` endpoint.
2. The system processes the documents and stores embeddings in the vector database.
3. Ask a question using the `/ask` endpoint.
4. The system retrieves relevant document chunks from the database.
5. The language model generates an answer based on the retrieved context.
6. The response includes the answer and the source documents.

---

## Advantages of the RAG Approach

* Reduces hallucinations in AI responses
* Enables domain-specific knowledge integration
* Allows real-time document querying
* Provides traceable answers with source attribution
* Supports scalable knowledge bases

---

## Future Improvements

Potential extensions for the project include:

* Support for additional document formats (DOCX, TXT)
* Advanced retrieval techniques (hybrid search)
* Frontend user interface
* Authentication and role-based access control
* Query analytics and logging
* Docker-based deployment
* Cloud deployment (AWS / GCP / Azure)

---

## Author

**Yasashwini Gollakoti**  
Software Engineer | Capgemini

---

## License

This project is developed for learning, experimentation, and demonstrating practical AI engineering concepts.