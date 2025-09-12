import os
import json
from dotenv import load_dotenv
import numpy as np
from pathlib import Path
from openai import OpenAI
import openai


# Load environment variables from .env
load_dotenv()

# Init OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("./data/APCHEM.txt", 'r') as f:
    content_pack = f.read()

# --- 3. Query function ---
def ask_cag_model(user_query):
    prompt = content_pack + f"\n\nUser: {user_query}\n\nAnswer:"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    # Extract text
    answer = response.choices[0].message.content
    return answer


query = "Hello"
answer = ask_cag_model(query)
print("Answer:\n", answer)