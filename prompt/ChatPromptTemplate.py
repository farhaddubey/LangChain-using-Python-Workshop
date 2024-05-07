import os

from dotenv import load_dotenv

load_dotenv() 
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain_openai import OpenAI

llm=OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello how are you doing?"), 
        ("ai", "I'm doing well thanks. "),
        ("human", "{user_input}"),
    ]
)
messages = chat_template.format_messages(name="Bob", user_input="What is your name?")
print(messages)

#For example, in addition to using the 2-tuple representation of(type, content) used above, We could pass in an instance of MessagePromptTemplate 
# or Base Message  
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate

chat_template=ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a helpful AI assistant that re-writes user's text to."
                "Sound more upbeat."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
messages = chat_template.format_messages(text="I don't like eating tasty things easily")
print(messages)