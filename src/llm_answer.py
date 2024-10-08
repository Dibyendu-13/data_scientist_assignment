# src/llm_answer.py

import requests
from utils.config import HUGGINGFACE_API_KEY


API_URL = "https://api-inference.huggingface.co/models/gpt2"  # Use a specific model like gpt2, or any other you prefer

def generate_answer(query, context):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": f"{query}\n{context}",
        "options": {
            "use_cache": False,
            "max_length": 150,  # Set maximum length for response
            "temperature": 0.7,  # Control randomness of output
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]['generated_text']  # Extract generated text
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
