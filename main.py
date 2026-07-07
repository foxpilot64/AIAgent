import os
import argparse
import sys

from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions, call_function





#define the main function
def main() -> None:

    #Parse arguments
    parser = argparse.ArgumentParser(description="AI chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
   
    #Load env/get API key
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY not found in this environment")
    
   
    #Build the messages list
    messages = [
        {
            "role": "system", "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        },
    ]


    #Create the client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    for _ in range(20):

    #Make the API call with messages
        response = client.chat.completions.create(
            model="tencent/hy3:free",
            messages=messages,
            tools=available_functions,
    )
    
        if not response.usage:
            raise RuntimeError("API response appears to be malformed")
    
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        
        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print(message.content)
            return
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)

    print("Max number of iterations reached")
    sys.exit(1)


        

if __name__ == "__main__":
    main()
