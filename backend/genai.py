from gradio_client import Client

# Connect to your HF Space
client = Client("angelycwingz/poet-gen-ai-space")

def gen_poem(prompt: str) -> str:
    try:
        # The api_name is usually "/predict" unless you renamed it in app.py
        result = client.predict(
            prompt,        # input value
            api_name="/predict"
        )
        return result
    except Exception as e:
        return f"Error calling HF Space: {e}"
    
# For standalone testing
if __name__ == "__main__":
    # Make sure to set your environment variable or replace HF_TOKEN above!
    prompt = "write a romantic poem on girl's eyes"
    print(gen_poem(prompt))

