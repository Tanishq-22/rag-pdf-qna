from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

for m in client.models.list():
    actions = m.supported_actions or []
    name = m.name.replace("models/", "")
    if "generateContent" in actions and "flash" in name:
        print(name)