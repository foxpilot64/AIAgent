import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)





#Create new list and set the only message(for now) as the user's prompt:
from google.genai import types
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("user_prompt") # for the prompt
parser.add_argument("--verbose", action ="store_true") # for --verbose flag

args = parser.parse_args()

messages = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")