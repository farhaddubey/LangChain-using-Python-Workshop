import os
from operator import itemgetter

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import (ChatMessagePromptTemplate, ChatPromptTemplate,
                               HumanMessagePromptTemplate)
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

# Example 1 - Chain
human_template = "tell me a fact about {topic}"
chat_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(human_template)
])

# chain = LLMChain(llm=chat, prompt=chat_prompt)
# chain = chat_prompt | chat 
chain = chat_prompt | chat | StrOutputParser()
# response = chain.invoke(input="javascript")
# Insted object can also be passed 
response = chain.invoke({"topic":"Java"})
print(response)

# Example 2 Multi Chains 
chat_prompt1 = ChatPromptTemplate.from_template(
    "What is the city {person} is from?"
)
chat_prompt2 = ChatPromptTemplate.from_template(
    "What country is the city {city} In? response in {language}"
)
city_chain = chat_prompt1 | chat |StrOutputParser()
country_chain =(
    {"city":city_chain, "language":itemgetter("language")} | chat_prompt2 | chat | StrOutputParser()
)
response = country_chain.invoke({"person":"Virat", "Language":"English"})
print(response)