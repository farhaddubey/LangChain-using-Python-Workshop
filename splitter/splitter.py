import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI, OpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

# Split by character
# This is a long document we can split up.
with open("./data/sample.txt") as f:
    sample_data = f.read()
print(sample_data)
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=200,
)

texts = text_splitter.create_documents([sample_data])
print(texts[0].page_content)