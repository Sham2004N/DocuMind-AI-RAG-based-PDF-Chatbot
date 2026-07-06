# 🤖 DocuMind AI – RAG-Based PDF Chatbot

An intelligent **Retrieval-Augmented Generation (RAG)** chatbot that enables users to upload PDF documents and ask natural language questions. The application retrieves relevant information from the uploaded documents using **FAISS** and **Sentence Transformers**, then generates accurate, context-aware responses with **Google Gemini 2.5 Flash**.

---

## 🚀 Features

- 📄 Upload one or multiple PDF documents
- 💬 Ask questions in natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using FAISS
- 📚 Document chunking and embedding generation
- 🤖 AI-powered responses using Gemini 2.5 Flash
- 🌐 Interactive Streamlit web interface
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash API
- FAISS
- Sentence Transformers
- PyPDF
- NumPy
- python-dotenv

---

## 📂 Project Structure

```
DocuMind-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   └── gemini.py
│
├── assets/
│   ├── home.png
│   ├── architecture.png
│   └── demo.gif
│
└── sample_pdfs/
    └── sample.pdf
```

---

## ⚙️ How It Works

1. Upload one or more PDF documents.
2. Extract text from the uploaded PDFs.
3. Split the text into smaller chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector database.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant document chunks.
8. Send the retrieved context along with the question to Gemini.
9. Display an accurate, context-aware response.

---

## 🏗️ Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
      Upload PDF / Ask Question
                  │
                  ▼
            PDF Processing
                  │
                  ▼
            Text Chunking
                  │
                  ▼
      Sentence Transformers
                  │
                  ▼
           FAISS Vector Store
                  │
                  ▼
       Retrieve Relevant Chunks
                  │
                  ▼
      Google Gemini 2.5 Flash
                  │
                  ▼
           Generated Response
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Multiple PDF retrieval
- Chat memory
- Streaming AI responses
- Source citations
- OCR support for scanned PDFs
- Voice input/output
- Cloud deployment
- Docker support

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- Prompt Engineering
- Streamlit
- Python
- FAISS
- Gemini API
- NLP

---

## 👨‍💻 Author

**Shyamkumar Nhavkar**

📧 Email: nhavkarsham@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/shyamnhavkar

---

## ⭐ If you found this project useful, consider giving it a star!
