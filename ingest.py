from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Step 1: Load document
print("Loading document...")
loader = TextLoader("sample_doc.txt")
documents = loader.load()
print(f"Loaded {len(documents)} document(s)")

# Step 2: Chunk it
print("Chunking...")
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")

# Step 3: Embed and store
print("Embedding and storing... (first run downloads a small model)")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
print("Done! Vector store saved to ./chroma_db")
print(f"Total chunks stored: {vectorstore._collection.count()}")