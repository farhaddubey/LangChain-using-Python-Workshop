import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI, OpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_openai import OpenAIEmbeddings

embeddings_model=OpenAIEmbeddings(openai_api_key=SECRET_KEY)
# text="Thsi is simple text"
# embedded_query = embeddings_model.embed_query(text)
# print(embedded_query)

texts = [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
embeddings= embeddings_model.embed_documents(texts)
len(embeddings)
print(embeddings[0])
