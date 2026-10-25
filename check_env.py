import os
from dotenv import load_dotenv

print("Looking in folder:", os.getcwd())
found = load_dotenv()
print(".env file found:", found)
key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", key is not None)