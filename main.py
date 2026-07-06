import os
from dotenv import load_dotenv
from openai import OpenAI



#define the main function
def main() -> None:
   
    #Load env/get API key
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY not found in this environment")
    
   
    #Build the messages list
    messages = [
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
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
    )

    #Keep track of token usage
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)
    print("Response:")
    
    print(response.choices[0].message.content)

  


if __name__ == "__main__":
    main()
