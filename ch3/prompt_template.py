# For importing the API key from .env file to connect with the OPENAI
import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')  


# Now making thee connection with openAI 
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)


#Now importing the prompt library 
# from langchain_core.prompts import PromptTemplate

# prompt_template=PromptTemplate.from_template(
#     "Tell me a {adjective} joke about {content}."
# )
# prompt_template.format(adjective="funny", content="chickens")
# print(prompt_template)
# this template supports any no. of variable including no variable 
from langchain_core.prompts import PromptTemplate

prompt_template=PromptTemplate.from_template("Tell me a Joke")
prompt_template.format()
print(prompt_template)
