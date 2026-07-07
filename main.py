import os
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
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
        model="tencent/hy3:free",
        messages=messages,
        tools=available_functions,
    )
    #Grab message, if set, iterate and print args, if none just print as normal
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            if not result_message["content"]:
                raise Exception("content empty")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(message.content)
  

    #Keep track of token usage
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    

 

  


if __name__ == "__main__":
    main()
