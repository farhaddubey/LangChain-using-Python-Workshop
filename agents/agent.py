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

# Agent Type  - Open AI Functions 
# After installing the pip now creataing the agent
prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt)
search = DuckDuckGoSearchRun()

tools = [search]
agent = create_openai_functions_agent(llm=chat, tools=tools, prompt=prompt)
#Running Agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke(
    {"input":"Who is current PM of India?"}
)
print(response)


# Using Decorator and Building Custom tool
@tool
def search(query:str) -> str:
    return "Langchain"
print(search.name)
print(search.description)
# print(search.)
 # Using Structure Tool 
class CalculatorInput(BaseModel):
   a: int = Field(description="first Number")
   b: int = Field(description="second Number")
def multiply(a:int, b:int) -> int:
  "Multiply two Numbers"
  return a*b 
calculator = StructuredTool.from_function(
  func=multiply,
  name="Calculator", 
  description="Multiply Numbers)", 
  args_schema=CalculatorInput,
  return_direct=True, 
)
print(calculator.name)
print(calculator.description)
print(calculator.args)
