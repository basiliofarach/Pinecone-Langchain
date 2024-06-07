from dataclasses import dataclass
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter


@dataclass
class TextChunk:
    file_path: str

    def divide_chunks(self):
        loader = TextLoader(self.file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        return text_splitter.split_documents(documents)