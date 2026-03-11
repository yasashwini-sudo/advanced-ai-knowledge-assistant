from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os


def create_qa_chain(vector_store):

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    # Better retriever for general documents
    retriever = vector_store.as_retriever(
    search_kwargs={"k":8}
)

    # Prompt to ensure answers come from document
    prompt_template = """
You are a helpful assistant answering questions based ONLY on the provided document context.

If the answer is not in the context, say:
"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa_chain