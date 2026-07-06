import streamlit as st

# Backend Modules
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.vector_store import create_vector_store
from utils.rag import retrieve_context
from utils.gemini import ask_gemini

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Assistant")
st.markdown(
    """
Ask anything or upload PDFs and chat with your documents using **Gemini + RAG**.
"""
)

# ---------------------------------------
# Session State
# ---------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.title("📄 PDF Upload")

uploaded_files = st.sidebar.file_uploader(
    "Upload one or more PDFs",
    type="pdf",
    accept_multiple_files=True
)

process_button = st.sidebar.button("📚 Process PDFs")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------------------------------
# Process PDFs
# ---------------------------------------

if process_button:

    if uploaded_files:

        with st.spinner("Reading PDF..."):

            text = load_pdf(uploaded_files)

            chunks = split_text(
                text,
                chunk_size=500,
                overlap=100
            )

            embeddings = create_embeddings(chunks)

            index = create_vector_store(embeddings)

            st.session_state.index = index
            st.session_state.chunks = chunks

        st.sidebar.success("✅ PDFs processed successfully!")

    else:
        st.sidebar.warning("Please upload at least one PDF.")

# ---------------------------------------
# Display Chat History
# ---------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------
# Chat Input
# ---------------------------------------

question = st.chat_input("Ask anything...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -------------------------------
    # RAG Mode
    # -------------------------------

    if st.session_state.index is not None:

        context = retrieve_context(
            question,
            st.session_state.index,
            st.session_state.chunks
        )

    else:

        context = ""

    # -------------------------------
    # Gemini Response
    # -------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_gemini(
                question=question,
                context=context
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ---------------------------------------
# Footer
# ---------------------------------------

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit • Gemini • FAISS • Sentence Transformers"
)