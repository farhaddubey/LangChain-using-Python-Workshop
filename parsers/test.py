import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain.output_parsers import (CommaSeparatedListOutputParser,
                                      DatetimeOutputParser,
                                      PydanticOutputParser)

# Example 1
date_time_parser = DatetimeOutputParser()
# print(date_time_parser.get_format_instructions())

comma_sep_parser = CommaSeparatedListOutputParser()
# print(comma_sep_parser.get_format_instructions())

from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
date_time_parser = DatetimeOutputParser()
human_template="{request}\n{format_instruction}"
chat_prompt=ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(human_template)
])
print("Chat Prompt: ", chat_prompt)
formatted_chat_prompt = chat_prompt.format_messages(
    request="What date was when World War 2 declared?",
    format_instruction=date_time_parser.get_format_instructions()
)
# print(formatted_chat_prompt)
# response=chat.invoke(formatted_chat_prompt)
# print("Response Content: ", response.content)
# print("Response Content Parse: ", date_time_parser.parse(response.content))
print("\n\n\n")

class Cricketer(BaseModel):
    name: str = Field(description="Name of Cricketer")
    records: list = Field(description="Python list of records")

parser = PydanticOutputParser(pydantic_object=Cricketer)
# print(parser.get_format_instructions())

human_template="{request}\n{format_instruction}"
chat_prompt = ChatPromptTemplate([
    HumanMessagePromptTemplate.from_template(human_template)
])

formatted_chat_prompt = chat_prompt.format_messages(
    request="Tell me about a Cricketer", 
    format_instruction=parser.get_format_instructions()
)
print(formatted_chat_prompt)
    
