import streamlit as st
import requests

# URL of your FastAPI backend (adjust if running on a different port/host)
# BACKEND_URL = "http://localhost:8000/generate"  
BACKEND_URL = "https://shakespearemuse.onrender.com/generate" # Replace with your actual backend URL


st.title("🎭 Shakespeare Muse")
st.write(
    "Enter a prompt and generate a poem using the backend GenAI model (powered by Perplexity AI)."
)

# User input area
prompt = st.text_area("Type your prompt here:", height=150)
generate_button = st.button("Generate")

# Placeholder for results and error messages
result_placeholder = st.empty()
error_placeholder = st.empty()

if generate_button:
    if not prompt.strip():
        error_placeholder.error("Please enter a prompt to generate your poem.")
    else:
        error_placeholder.empty()
        with st.spinner("Wait a while, good poetry takes some time...."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={"prompt": prompt},
                    timeout=70,  # Increase timeout for slow API responses
                )

                if response.status_code != 200:
                    result_placeholder.error(
                        f"API Error: {response.status_code} | {response.text}"
                    )

                else:
                    data = response.json()
                    generated = data.get("generated_text", "")
                    result_placeholder.success("**Generated Text:**\n\n" + generated)
                
            except Exception as e:
                result_placeholder.error(f"Request failed: {str(e)}")