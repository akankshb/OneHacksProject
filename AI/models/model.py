import os
import json
from dotenv import load_dotenv
import numpy as np
from pathlib import Path
from openai import OpenAI
import openai

# --- 3. Query function ---
def ask_cag_model(user_query):
    load_dotenv()

    # Init OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with open("./AI/data/APCHEM.txt", 'r') as f:
        content_pack = f.read()

        prompt = content_pack + f"\n\nUser: {user_query}\n\nAnswer:"
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    # Extract text
    answer = response.choices[0].message.content
    return answer


def query():
    # Example: run a query
    user_query = input("Enter your question: ")
    answer = ask_cag_model(user_query)
    print("\nModel Answer:\n", answer)


if __name__ == "__main__":
    query()