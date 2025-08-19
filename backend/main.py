from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from genai import gen_poem
from schemas import PromptRequest, GeneratedText

app = FastAPI()

# Allow requests from your deployed Streamlit frontend
origins = [
    "https://shakespearemuse-v5z49agfgjgvj2l5pmyi3j.streamlit.app" # Replace with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development: allows all. For production, specify your frontend origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=GeneratedText)
async def generate_text(prompt: PromptRequest) -> GeneratedText:
    # Here you would typically call your text generation model
    # For demonstration, we will just return the prompt back
    generated_response = gen_poem(prompt.prompt)
    return GeneratedText(generated_text=generated_response)