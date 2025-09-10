from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from genai import gen_poem
from schemas import PromptRequest, GeneratedText

app = FastAPI()

# Allow requests from your deployed Streamlit frontend
origins = [
    "https://shakespearemuse.streamlit.app","http://localhost:8501/" # Replace with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # For development: allows all. For production, specify your frontend origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=GeneratedText)
async def generate_text(request: PromptRequest) -> GeneratedText:
    generated_response = gen_poem(request.prompt)
    print("Generated response:", generated_response)

    return GeneratedText(generated_text=generated_response)