import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI, OpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

#Loading Document 
loader = TextLoader('./data/history.txt')
history_doc=loader.load()

#Splitting Document
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
history_document=text_splitter.split_documents(history_doc)

#Embedding Model Object 
embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)

#Store 
db = Chroma.from_documents(history_doc, embedding_function)
query="AI programming focuses on cognitive skills "
 
 # We can use it or We can use Retriever...
# similar_docs = db.similarity_search(query)
retriever=db.as_retriever()
similar_docs=retriever.get_relevant_documents(query)
print(similar_docs)





