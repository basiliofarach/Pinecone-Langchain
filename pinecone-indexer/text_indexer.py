import os
import time
from dataclasses import dataclass
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from text_chunks import TextChunk
import getpass

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

pc = Pinecone(
    api_key = os.environ.get("PINECONE_API_KEY"),
)

@dataclass
class TextIndexer:
    index_name: str
    file_path: str
    def index(self):
        docs_chunks = TextChunk(self.file_path).divide_chunks()
        embeddings = OpenAIEmbeddings()

        existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

        if self.index_name not in existing_indexes:
            pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not pc.describe_index(self.index_name).status["ready"]:
                time.sleep(1)

        pc.Index(self.index_name)
        #create a new index
        PineconeVectorStore.from_documents(docs_chunks, embeddings, index_name=self.index_name)