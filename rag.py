from utils.embeddings import create_embeddings #Used to convert the user's question into an embedding.
from utils.vector_store import search_chunks   #Searches the FAISS database.


def retrieve_context(query, index, chunks):
    """
    Retrieve the most relevant chunks for the user's query.
    """

    query_embedding = create_embeddings([query]) #Create Query Embedding

    retrieved_chunks = search_chunks(   #FAISS compares the question with every stored chunk.
        query_embedding,
        index,
        chunks,
        top_k=3
    )

    context = "\n\n".join(retrieved_chunks)

    return context