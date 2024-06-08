from dataclasses import dataclass
from llm.pinecone_reader import PineconeReader
import openai

@dataclass
class LangchainPrompt:
    pinecone_reader: PineconeReader
    openai_api_key: str
    openai_model: str

    def generate_response(self, query_text: str) -> str:
        results = self.pinecone_reader.query_index(query_text)
        if results['matches']:
            response_content = "What you were looking for is this: \n" + "\n".join(
                [f"ID: {match['id']}, Score: {match['score']}" for match in results['matches']]
            )
        else:
            response_content = "I couldn't find relevant information. Please provide more details."

        return self.get_llm_response(response_content)

    def get_llm_response(self, input_text: str) -> str:
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(
            engine=self.openai_model,
            prompt=(
                "You are a powerful LLM. Try to read from the vector. "
                "If you obtain a response, make a response like this:\n\n"
                "What you were looking for is this: {response}\n\n"
                "And if you do not find it, please ask the user to add more information."
            ).format(response=input_text),
            max_tokens=150
        )
        return response.choices[0].text.strip()
