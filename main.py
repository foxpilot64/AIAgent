import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=["Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."]
)

print(response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)

print("This script is called:", sys.argv[0])
print("Arguments passed", sys.argv[1:])

if len(sys.argv) < 2:
    print("Error,no prompt detected... ")
    sys.exit(1) #Exits script with error code 1

