# 📚 RAG Document Chatbot – Ask Questions About Your Documents

![Streamlit](https://img.shields.io/badge/Streamlit-1.55.0-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?logo=chainlink)
![Gemini](https://img.shields.io/badge/Gemini_API-2.5_Flash-4285F4?logo=google)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.5+-8A2BE2)

> Upload any PDF or text file, ask questions, and get answers grounded in your document.  
> Built with **LangChain**, **ChromaDB**, **HuggingFace embeddings**, and **Google Gemini 2.5 Flash**.

---

## 🌐 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-chatbot-6uqiby4vpj26gzud3uipj6.streamlit.app/)

---

## ✨ Features

- 📄 Upload **PDF** or **TXT** documents
- 🔍 Automatically splits the text into semantic chunks
- 🧠 Uses **HuggingFace embeddings** (`all-MiniLM-L6-v2`) to create vector representations
- 💾 Stores chunks in **ChromaDB** for fast similarity search
- 🤖 Retrieves the most relevant chunks and passes them to **Gemini 2.5 Flash**
- ✅ Answers are grounded in your document – no hallucinations
- 🖥️ Simple **Streamlit** interface with source chunk preview

---

## 🛠️ Tech Stack

| Component           | Technology                                 |
|---------------------|--------------------------------------------|
| **Framework**       | Streamlit                                  |
| **LLM**             | Google Gemini 2.5 Flash                    |
| **Embeddings**      | HuggingFace `all-MiniLM-L6-v2` (free)     |
| **Vector DB**       | ChromaDB (local persistent storage)        |
| **Document Loaders**| PyPDF2 / TextLoader (LangChain)            |
| **Chunking**        | RecursiveCharacterTextSplitter             |
| **Retrieval**       | ChromaDB similarity search                 |

---

## 🚀 Getting Started (Run Locally)

### 1. Clone the repository
```bash
git clone https://github.com/himanshusarohaa/rag-chatbot.git
cd rag-chatbot
2. Create and activate a virtual environment
bash


Download
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install dependencies
bash


Download
pip install -r requirements.txt
4. Set up your Gemini API key
Create a file named .env in the project root and add:


Download
GEMINI_API_KEY=AIzaSy...
Never commit this file. It is already listed in .gitignore.

5. (Optional) Pre‑index a sample document
The repository includes sample_doc.txt. You can index it with:

bash



Download
python ingest.py
This will create the chroma_db/ folder locally.

6. Run the app
bash


Download
streamlit run app.py
Your browser will open at http://localhost:8501.

📁 Project Structure
text


Download
rag-chatbot/
├── app.py                 # Streamlit UI with file upload and Q&A
├── ingest.py              # Script to index a document (optional)
├── query.py               # Terminal‑based retrieval test
├── sample_doc.txt         # Example document
├── requirements.txt       # Python dependencies
├── .env                   # (ignored) API key
├── .gitignore             # Excludes .env, chroma_db/, etc.
└── README.md              # This file

🧠 How It Works
Document Upload – User uploads a PDF or TXT.
Chunking – The document is split into overlapping chunks (size 400, overlap 60).
Embedding – Each chunk is converted into a vector using a free sentence‑transformer model.
Vector Store – All vectors are stored in a ChromaDB collection.
Question – User asks a question.
Retrieval – The top‑3 most similar chunks are retrieved from ChromaDB.
Generation – The chunks are sent to Gemini along with the question, with a prompt to answer only using the context.
Answer – The LLM returns a grounded answer, and the source chunks are shown.
This is the exact architecture used in modern enterprise RAG systems.

🔒 Environment Variables
Variable	Description
GEMINI_API_KEY	Your Google Gemini API key
On deployment (Streamlit Cloud), add this key in the Secrets section.

📬 Contact
Himanshu Saroha
GitHub: @himanshusarohaa

🙏 Acknowledgements
LangChain
ChromaDB
HuggingFace
Google Gemini
Streamlit
