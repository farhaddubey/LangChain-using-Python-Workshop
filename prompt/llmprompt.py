import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
# print(SECRET_KEY)
# chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
llm = OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

# LLMs - Prompt Template 
# Example 1 - Prompt having no Input Variable 
noInputPrompt=PromptTemplate(input_variables=[], template="Tell me a Py Trick")
formattedNoInputPrompt = noInputPrompt.format()
# print("No Input Prompt: ", formattedNoInputPrompt)

response = llm.invoke(formattedNoInputPrompt) 
print("Response: ", response)


# Example 3: Prompt having Multiple input variable 
multipleInputPrompt = PromptTemplate.from_template(
    input_variables=["language", "topic"], template=
    "Tell me a {language} {topic} Trick")
