import chromadb
from chromadb.config import Settings
import os
from typing import List, Dict, Any

class ChromaDBService:
    def __init__(self, persistence_path: str = "data/knowledge"):
        self.client = chromadb.PersistentClient(path=persistence_path)
        self.collection_name = "bali_knowledge"
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def add_documents(self, documents: List[str], metadatas: List[Dict[str, Any]], ids: List[str]):
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_text: str, n_results: int = 3) -> Dict[str, Any]:
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def count(self):
        return self.collection.count()

chroma_service = ChromaDBService()
