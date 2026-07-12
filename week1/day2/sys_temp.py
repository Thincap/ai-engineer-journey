import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my clothing company. name should be in one word"

message_system={
    "role": "system",
    "content": "You are a brand manager who suggests name for my clothing company. name should be in one word"
}

message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

# Temperature by default is 0 meaning safe, can increase to 2 for more creative responses , range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, temperature=1)

answer= response.choices[0].message.content
print(answer)




