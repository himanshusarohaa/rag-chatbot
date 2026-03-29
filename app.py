# app.py – full RAG chatbot with file upload
import streamlit as st
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv
import os
import tempfile

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="RAG Document Chatbot")
st.title("📚 RAG Document Chatbot")
st.write("Upload a document (PDF or TXT) and ask questions. Powered by LangChain + ChromaDB + Gemini.")

uploaded = st.file_uploader("Choose a file", type=["pdf", "txt"])

if uploaded:
    # Save uploaded file to a temp file
    suffix = ".pdf" if uploaded.name.endswith(".pdf") else ".txt"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.read())
        path = tmp.name

    with st.spinner("Processing document..."):
        # Load document based on type
        if suffix == ".pdf":
            loader = PyPDFLoader(path)
        else:
            loader = TextLoader(path)
        docs = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
        chunks = splitter.split_documents(docs)

        # Embed and store in a temporary vector store
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vs = Chroma.from_documents(chunks, embeddings)

        st.success(f"Ready! Indexed {len(chunks)} chunks from your document.")

    # Question input
    q = st.text_input("Ask a question about the document:")

    if q:
        with st.spinner("Thinking..."):
            # Retrieve relevant chunks
            retrieved = vs.similarity_search(q, k=3)
            context = "\n\n".join([d.page_content for d in retrieved])
            prompt = f"Answer using only this context:\n{context}\n\nQuestion: {q}"
            answer = model.generate_content(prompt).text

            st.subheader("Answer")
            st.write(answer)

            with st.expander("Source chunks retrieved"):
                for i, d in enumerate(retrieved):
                    st.write(f"Chunk {i+1}: {d.page_content[:200]}...")