import os
import azure.functions as func
import logging
import json
import logging

from langchain_openai import OpenAIEmbeddings
from llm.llm_openai import LangchainPrompt
from llm.pinecone_reader import PineconeReader

# Replace with your actual API key, environment, and index name
api_key = os.environ.get("PINECONE_API_KEY")
environment = os.environ.get("PINECONE_ENVIRONMENT")
index_name = os.environ.get("PINECONE_INDEX_NAME")
embeddings = OpenAIEmbeddings()  
openai_api_key = os.environ.get("PINECONE_INDEX_NAME")
openai_model = os.environ.get("OPENAI_API_KEY")

reader = PineconeReader(api_key, environment, index_name, embeddings)
prompt = LangchainPrompt(pinecone_reader=reader, openai_api_key=openai_api_key, openai_model=openai_model)


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')

    try:
        req_body = req.get_json()
        query_text = req_body.get('query')

        if not query_text:
            return func.HttpResponse(
                "Please pass a query in the request body",
                status_code=400
            )

        response = prompt.generate_response(query_text)
        return func.HttpResponse(response, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(
            "Error processing request",
            status_code=500
        )