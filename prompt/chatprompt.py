import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

# Chat Model - Prompt Template 

# Example 1 - Message Prompt Template as Tuples 
from langchain_core.prompts import (AIMessagePromptTemplate,
                                    ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)

chatPrompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpgul assistant that translates {input_language} to {output_language}"),
    ("human", "{text}")
])
print("Chat Prompt Input Variables: ", chatPrompt.input_variables)
formattedChatPrompt=chatPrompt.format_messages(
    input_language="English", 
    output_language="French",
    text="I am learning LangChain JS from Geekyshows YT"
)
print(formattedChatPrompt)



llm = OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)


### Example 2: Using Message Classes 
sys_template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template="{text}"
chatPrompt=ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(sys_template),
    HumanMessagePromptTemplate.from_template(human_template)
])
print("Chat Prompt:   ", chatPrompt)
print("INput Variables:  ", chatPrompt.input_variables)
print("\n")
formattedChatPrompt=chatPrompt.format_messages(
    input_language="English",
    output_language="French",
    text="I am learning LangChain JS from GeekyShows YT"
)
print("Formatted Chat Prompt: ", formattedChatPrompt)
response = llm.invoke(formattedChatPrompt)
print("Response:\n", response)
print("\n", response.content)