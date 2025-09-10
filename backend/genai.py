from fastapi import HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "YOUR_PERPLEXITY_API_KEY_HERE")

# if not PERPLEXITY_API_KEY:
#     raise RuntimeError("❌ PERPLEXITY_API_KEY not set in environment. Please configure it in .env or your host settings.")


def gen_poem(prompt: str) -> str:

    print("Using API Key:", PERPLEXITY_API_KEY[:6] + "..." if PERPLEXITY_API_KEY else "None")

    model = "sonar-pro"

    url = "https://api.perplexity.ai/chat/completions"

    headers = {
    "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
    "Content-Type": "application/json"
    }
    
    payload = {
    "model": model,
    "messages": [
        {
            "role": "system",
            "content": """You are a world class poet who writes modern beautiful poems inspired by Shakespeare. 
                        You are to answer the user's prompts by generating a poem that is creative, engaging, and evocative. 
                        Your responses should be in English and should capture the essence of the prompt while adhering to the 
                        stylistic elements of Shakespearean poetry. Use rich imagery, metaphor, and classical references to enhance 
                        the quality of your poems. Always aim to inspire and move the reader with your words. NOT more than 400 character.
                      """
        },
        {
            "role": "user",
            "content": f"Generate a poem based on the following prompt: {prompt}"
        }
    ]}

    response = requests.post(url, json=payload, headers=headers)

    print("Perplexity API response status:", response.status_code)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error from Perplexity API: {response.text}")

    try:
        poem = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error Parsing poem content: {e}"
    
    return poem.strip()
    

