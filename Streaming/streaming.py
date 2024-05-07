import os

import langchainhub
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate)
from langchain_openai import ChatOpenAI

from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

chat_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template("Tell me a how to convience for fun to a  {topic}")
])
formatted_chat_promt=chat_prompt.format_messages(topic="Hot Female")
# response = chat.invoke(formatted_chat_promt)
response = chat.stream(formatted_chat_promt)
# for res in response:
#     print(res.content, end="'", flush=True)
print(response)

# Straming in Chain
chat_prompt=ChatPromptTemplate.from_template("Telll me a face about {topic}")
chain = chat_prompt | chat | StrOutputParser() 
response = chain.stream({"topic": "Python"})
for res in response:
    print(res.content, end="", flush=True)