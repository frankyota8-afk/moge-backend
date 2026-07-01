# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def get_embedding(text):
#     return model.encode(text).tolist()




#<!--===================================
#   GEMINI EMBEDDING MODEL
#====================================-->
from google import genai
from google.genai import types

client = genai.Client()

def get_embedding(text):
    # Use 'text-embedding-004' for standard text or 'gemini-embedding-2' for multimodal
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT" # Optional: specify based on your use case
        )
    )
    # The API returns a list of embeddings; extract the values
    return response.embeddings[0].values
