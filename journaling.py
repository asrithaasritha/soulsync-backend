import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("✅ Loaded GEMINI API Key:", api_key)

def generate_reflection(entry):
    API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": api_key
    }
    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"You are an empathetic journaling assistant. Respond supportively to this journal entry:\n\n{entry}"
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, params=params, json=body)
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("❌ Error:", e)
        return "⚠️ Something went wrong. Please try again."
