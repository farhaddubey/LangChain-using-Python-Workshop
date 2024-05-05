import os

from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
print(SECRET_KEY)

# LLMS
# llm = OpenAI(api_key=SECRET_KEY)
# response=llm.invoke("Who is PM of India")
# print(response)

# Example 2 
from langchain_core.messages import HumanMessage, SystemMessage
# ChatModel 
from langchain_openai import ChatOpenAI

# Example 1
# chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
# response=chat.invoke("Who si PM of India?")
# print(response)
# print(response.content)
chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
messages = [
    SystemMessage(content="You're a standup flirty comedian"),
    HumanMessage(content="Who is the PM of India?")
]
# Now the messages will be displayed............
response=chat.invoke(messages)
print(response)

for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)
print(chat.batch([messages]))
# Now the messages in batch will be displayed............ 
# await chat.ainvoke(messages) 
