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

from pydantic import BaseModel
class CustomerComplaint(BaseModel):
    name:str
    email:str
    issue:str

schema= CustomerComplaint.model_json_schema()

response_format ={
    "type": "json_object"
}

system_promt=f"""
Extract the personal information from the customer complaint ticket and return it in the following JSON format:
{schema}
"""

message_system={
    "role": "system",
    "content": system_promt
}

text="Hello, My name is Parikshit, I live in india, I am a software engineer and i have bought an iphone 15 pro max from your store  but it not working also it got broked, this is my emailid abc@gmail.com and my phone number is 5643589858934, i want solution for this issue, please help me out. This is my address: 123, xyz street, abc city, india, 123456. Please help me out to resolve this issue as soon as possible."
prompt=f"""
This is an customer complaint ticket. Please extract the personal information for this
{text}
"""

message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages,response_format=response_format)

answer= response.choices[0].message.content
print(answer)
print("############################################################")



# How to read the required data from this response
import json
raw_json=answer
data_file=json.loads(raw_json)
complaint=CustomerComplaint(**data_file)

print(complaint.name)
print(complaint.email)
print(complaint.issue)


