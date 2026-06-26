import os
from dotenv import load_dotenv
import sys
import argparse
from google import genai
from google.genai import types
from prompts import system_prompt


#define the main function
def main() -> None:
    #Parse arguments
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="user_prompt")
    args = parser.parse_args()
   
    #Load env/get API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    #Build the messages list
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]


    #Create the client
    client = genai.Client(api_key=api_key)
    #Make the API call with messages
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0
        ),
    )

    #check tokens
    if not response.usage_metadata:
        raise RuntimeError("Something went wrong!")

    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)

    print(response.text)


if __name__ == "__main__":
    main()
