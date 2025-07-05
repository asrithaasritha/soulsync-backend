import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

response = requests.get(
    "https://generativelanguage.googleapis.com/v1beta/models",
    params={"key": api_key}
)

print(response.json())
