"""
Sends a message to the OpenAI API and appends both user and assistant messages to the session history.

Args:
    message (str): The user's message to the assistant.

Returns:
    None. Prints the assistant's reply to the console.
"""

from openai import OpenAI
from config import API_KEY as key

class NoKey(Exception):
    """Custom exception for missing API key."""
    pass
try:
    if key.strip() == "":
        raise NoKey
    messages = []

    client = OpenAI(
        api_key=key,  # This is the default and can be omitted
    )

    def completion(message):
        global messages
        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        chat_completion = client.chat.completions.create( messages=messages,
                            model="gpt-4o"
                            )
        
        # print(chat_completion)
        message = {
            "role": "assistant",
            "content": chat_completion.choices[0].message.content
        }
        messages.append(message)
        print(f"Assistant: {message["content"]}")

    if __name__ == "__main__":
        print(f"Assistant: Hi I am available, How may I help you...\n")
        while True:
            user_question = input()

            if user_question.lower() in ["exit", "quit", "bye"]:
                print("Assistant: Goodbye!")
                break
            
            elif user_question.strip() == "":
                print("Assistant: Please ask a valid question.")
                continue
            
            print(f"User: {user_question}")
            completion(user_question)

except NoKey:
    print("Error: API key is missing. Please set the Api_key in config.py.")    
except Exception as e:
    print(f"An error occurred: {e}")
    # This will catch any other exceptions that may occur, such as network issues or API errors.
