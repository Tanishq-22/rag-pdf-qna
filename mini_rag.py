import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

MODELS = ["gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.8-flash"]

def ask_llm(prompt, rounds=3):
    for round_number in range(rounds):
        for model in MODELS:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                print("(answered by", model + ")")
                return response.text
            except Exception as e:
                print(f"{model} failed: {str(e)[:80]}")
        print("All models busy, waiting 10 seconds...")
        time.sleep(10)
    return "The AI service is busy. Please try again later."

context = """
Page 3: The notice period for ending the rental agreement is 60 days.
Page 7: The security deposit is two months' rent.
"""

question = "What is the monthly rent?"

prompt = f"""Answer using ONLY the context below.
If the answer is not in the context, say "I couldn't find this in the document."
Cite the page number.

Context:
{context}

Question: {question}"""

print("Question:", question)
print("Answer:", ask_llm(prompt))