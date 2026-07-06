from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("Gemini_api_key")
)


def ask_gemini(question, context=""):
    """
    Generate an answer using Gemini.
    """

    prompt = f"""
You are a helpful AI assistant.

Use the context below to answer the user's question.

If the answer is not found in the context,
use your general knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text