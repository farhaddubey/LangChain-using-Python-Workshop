import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import (ChatMessageHistory,
                              ConversationBufferWindowMemory,
                              ConversationEntityMemory,
                              ConversationSummaryBufferMemory)
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from pydantic import BaseModel

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

ChatMessageHistory 
history = ChatMessageHistory()
history.add_user_message("Hi! there")
history.add_ai_message("Hello! What's up?")
print(history)


memory = ConversationBufferWindowMemory()
memory.save_context({"input": "Hello"}, {"output":"Hi What's up?"})
print(memory)

memory = ConversationBufferWindowMemory()
converation = ConversationChain(llm=chat, memory=memory, verbose=True)
converation.predict(input="Hi there")
converation.predict(input="Who's Modi?")
print(memory.buffer)

# Using ConversationBufferWindowMemory in Chaiin  
memory = ConversationBufferWindowMemory(k=1)
conversation = ConversationChain(llm=chat, memory = memory, verbose=True)
conversation.predict(input="Hi there")
conversation.predict(input="Who's PM")
print(memory.buffer)

# ConversationEntiyMemory
memory = ConversationEntityMemory(llm=chat)
conversation=ConversationChain(
    llm=chat, memory=memory,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, verbose=True
)
conversation.predict(input="Rohit & Gill are working on a hackathon project")
conversation.predict(input="They are trying to add more complex memory structures to Langchain")
conversation.predict(input="They are adding in a key-value store for entitites mentioned so far in the conversation")
conversation.predict(input="What do you know about Rohit?")
print(memory.buffer)


# ConversationSummaryBufferMemory
memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=50)
conversation_with_summary=ConversationChain(llm=chat, memory=memory, verbose=True)
conversation_with_summary.predict(input="Why people are scared of AI?")
print(memory.load_memory_variables({}))