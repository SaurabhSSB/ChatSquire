from openai import OpenAI
from config import Api_key as key

class NoKey(Exception):
    """Custom exception for missing API key."""
    pass

try:
  if key.strip() == "":
     raise NoKey
  client = OpenAI(api_key=key)

  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Skills required for a data scientist"
        }
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1
  )

  print(response.choices[0].message.content)
  # This code uses the OpenAI API to create a response based on a user input.
  # Note: The API key used here is a placeholder and should be replaced with a valid key.

except NoKey:
   print("Error: API key is missing. Please set the Api_key in config.py.")
except Exception as e:  
    print(f"An error occurred: {e}")
    # This will catch any other exceptions that may occur, such as network issues or API errors. 