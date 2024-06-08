from dataclasses import dataclass, field
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone


@dataclass
class PineconeReader:
    api_key: str
    environment: str
    index_name: str
    embeddings = OpenAIEmbeddings()
    index: Pinecone.Index = field(init=False, repr=False)

    def __post_init__(self):
        Pinecone(api_key=self.api_key, environment=self.environment)
        self.index = Pinecone.Index(self.index_name)

    def query_index(self, query_text, top_k=5):
        query_vector = self.embeddings.embed(query_text)
        results = self.index.query(query_vector, top_k=top_k)
        return results
