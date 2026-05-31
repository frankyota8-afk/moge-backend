import uuid
from pypdf import PdfReader
from .embeddings import get_embedding
from .chroma_db import doc_collection

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, size=500, overlap=100):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size - overlap
    return chunks

def store_document(file_path):
    text = load_pdf(file_path)
    chunks = chunk_text(text)

    for chunk in chunks:
        doc_collection.add(
            ids=[str(uuid.uuid4())],
            embeddings=[get_embedding(chunk)],
            documents=[chunk],
            metadatas=[{"source": file_path}]
        )

def retrieve_docs(query, k=5):
    results = doc_collection.query(
        query_embeddings=[get_embedding(query)],
        n_results=k
    )
    return results["documents"][0]