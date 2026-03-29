# query.py – test retrieval and answer generation
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Load vector store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

def ask(question):
    # Retrieve top 3 relevant chunks
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([d.page_content for d in docs])
    prompt = f"""
Answer using ONLY the context provided below.
If the answer is not in the context, say so honestly.

Context:
{context}

Question: {question}
"""
    response = model.generate_content(prompt)
    return response.text, docs

# Test
question = "What is RAG and how does it work?"
answer, sources = ask(question)
print("Q:", question)
print("A:", answer)
print("Chunks used:", len(sources))