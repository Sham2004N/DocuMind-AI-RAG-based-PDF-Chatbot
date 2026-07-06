#Imports the embedding model
from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Convert text chunks into embeddings.
    """

    embeddings = model.encode(chunks)

    return embeddings