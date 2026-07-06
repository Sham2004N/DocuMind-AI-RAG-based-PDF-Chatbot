import faiss       #Imports the vector search library.
import numpy as np #FAISS works with NumPy arrays.


def create_vector_store(embeddings):
    """
    Create a FAISS index and store embeddings.
    """

    embeddings = np.array(embeddings).astype("float32")  #Convert Data Type
                                                         #FAISS requires vectors in float32 format.
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)   #It compares vectors using Euclidean Distance

    index.add(embeddings)   #Stores every chunk vector.

    return index


def search_chunks(query_embedding, index, chunks, top_k=3):
    """
    Search the most relevant chunks.
    """

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results