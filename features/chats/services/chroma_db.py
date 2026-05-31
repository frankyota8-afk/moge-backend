import chromadb

client = chromadb.Client()

chat_collection = client.get_or_create_collection(name="chat_memory")
doc_collection = client.get_or_create_collection(name="documents")