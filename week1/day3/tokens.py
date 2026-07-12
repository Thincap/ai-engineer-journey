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

prompt1 = "Hey!"
prompt2 = "Explain time travel in detail under 100 words"
prompt3 = "Write a 1000 word essay on the history of AI"

prompt="Suggest a name for my clothing company. name should be in one word"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=100)
    usage = response.usage
    print(f"Prompt: {prompt} --> your tokens : {usage.prompt_tokens}, completion tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens}, Finish reason: {response.choices[0].finish_reason}")





