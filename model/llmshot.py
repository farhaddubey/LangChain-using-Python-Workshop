import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv("OPENAI_API_KEY")
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

llm =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

# LLMs
# Few Shot Examples 
examples = [
    {
        "input": """The patient presented with acute exacerbation of chronic obstructive pulmonay disease, manifesting symptoms such as dyspea, 
        increased respiratory rate, and use of accessory muscles for breathing.""",
        "output": """The patient is having a sudden worsening of chronic lung disease. This shows with difficulty breathing, faster breathing, and using extra muscles to breathe."""
    },
    {
        "input": """The patient is experiencing hyperlipidemia, characterized by elevated levels of low-density lipoprotein cholesterol and triglycerides, along with reudced high-density lipoprotein cholesterool, putting them at increased risk for cadiovascular disease""",
        "output": """"The patient has high cholesterol, with too much of the 'bad', kind and triglycerides, and not enough of the 'good' kind. This increases the risk of heart problems."""
    }
]
example_prompt = PromptTemplate(
    input_variables=["input", "output"], template="{input}\n{output}"
)
# myprompt=example_prompt.format(**examples[0])
# print(myprompt)
prompt=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt ,
    suffix="{myinput}",
    input_variables=["myinput"]
)
myprompt = prompt.format(
    myinput="""The patient presented with acute exacerbation of chronic obstructive pulmonay disease, manifesting symptoms such as dyspea, 
        increased respiratory rate, and use of accessory muscles for breathing."""
)
print(myprompt)

response=llm.invoke(myprompt)
print("Response: \n",response)