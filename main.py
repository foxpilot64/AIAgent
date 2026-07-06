import os
import argparse
import json
from prompts import system_prompt
from call_function import available_functions
from dotenv import load_dotenv
from openai import OpenAI



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
    #Make the API call with messages
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    #Grab message, if set, iterate and print args, if none just print as normal
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(message.content)

    #Keep track of token usage
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    

    
    print(response.choices[0].message.content)

  


if __name__ == "__main__":
    main()
