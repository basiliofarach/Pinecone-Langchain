# Pinecone and Langchain Integration with Azure Functions

This project demonstrates how to integrate Pinecone's vector store with Langchain and Azure Functions. It includes two main components:
1. A Timer Trigger Function that indexes documents into Pinecone vectors daily.
2. An HTTP Trigger API that responds to queries by reading from those vectors.

## Overview

### Timer Trigger Function

The Timer Trigger Function runs once a day and creates vectors in Pinecone for the indexed documents. This ensures that the vector store is regularly updated with the latest data.

### HTTP Trigger API

The HTTP Trigger API accepts queries and retrieves relevant information from the Pinecone vector store. It uses Langchain to generate responses. If no relevant information is found, it prompts the user to provide more details.

## Current Status

**Note:** This project is mostly functional but not fully operational due to the lack of access to Azure OpenAI. A few tweaks are required to make it fully functional.

## Requirements

- Azure Functions Core Tools
- Python 3.8+
- Pinecone API Key
- An Embedding Function compatible with Langchain
- (Optional) Access to Azure OpenAI for generating responses

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Install the required packages using the command:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Pinecone Setup

Replace the placeholders in the code with your actual Pinecone API key, environment, and index name.

### Embedding Function

Replace the placeholder with your actual embedding function in the code.

### Azure OpenAI Setup (Optional)

If you have access to Azure OpenAI, replace the placeholders with your actual API key and model in the code.

## How to Run

1. Ensure all dependencies are installed.
2. Configure your Pinecone API key, environment, index name, embedding function, and (optional) Azure OpenAI settings.
3. Deploy the Azure Functions to your Azure account.
4. The Timer Trigger Function will automatically run once a day to index documents.
5. Use the HTTP Trigger API to query the indexed vectors and receive responses.

## Note

Since you do not have access to Azure OpenAI, the provided code will not be fully functional without it. Once you have access, you can make the necessary tweaks to integrate Azure OpenAI for generating responses.

Feel free to modify and extend the code as per your requirements.
