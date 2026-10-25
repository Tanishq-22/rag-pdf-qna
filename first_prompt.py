import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

MODEL = "gemini-3.6-flash"

def ask_llm(prompt, retries=4):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt * 3)
    return "The AI service is busy. Please try again later."

print("Starting...")
answer = ask_llm("You are a strict teacher. Explain what a variable is to a 10-year-old.")
print("Answer:", answer)