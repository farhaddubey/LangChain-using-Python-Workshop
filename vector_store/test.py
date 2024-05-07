import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

# # Example 1 
# # Load Document 
# loader =TextLoader('./data/history.txt')
# history_doc=loader.load()
# #Split Document 
# text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
# history_document = text_splitter.split_documents(history_doc)
# #Embed Model Object 
# embedding_function = OpenAIEmbeddings(openai_api_type=SECRET_KEY)
# #Store 
# db = Chroma.from_documents(history_document, embedding_function)
# query="Why is artificial intelligence important?"
# # similar_docs = db.similarity_search(query)
# # print(similar_docs[0].page_content)

# #Using Vector Store Retriever 
# retriever = db.as_retriever()
# similar_docs = retriever.get_relevant_documents(query)
# print(similar_docs[0].page_content)

# # Here Nothing is saved Now observing towards How it can be saved?? 


# Example 2 
# Load Document 
loader =TextLoader('./data/history.txt')
history_doc=loader.load()
#Split Document 
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
history_document = text_splitter.split_documents(history_doc)
#Embed Model Object 
embedding_function = OpenAIEmbeddings(openai_api_type=SECRET_KEY)
#Store 
db = Chroma.from_documents(history_document, embedding_function, persist_directory="./chroma_db")
db.persist()
# Reading from Chroma DB 
db_connection = Chroma(embedding_function=embedding_function, persist_directory="./chro_db")
query="Why is artificial intelligence important?"
# similar_docs = db.similarity_search(query)
# print(similar_docs[0].page_content)

# Using Vector Store Retriever 
retriever = db_connection.as_retriever(search_kwargs={"k":2})
similar_docs = retriever.invoke(query)
print(similar_docs)

# Here Nothing is saved Now observing towards How it can be saved?? 
