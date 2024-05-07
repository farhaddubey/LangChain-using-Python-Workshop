import os

import langchainhub
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)