import os

from dotenv import load_dotenv
from langchain_core.prompts import (ChatPromptTemplate,
                                    FewShotChatMessagePromptTemplate)
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

# Chat Model 
# Few Shot Examples 
# Now defined examples that i would like to include 
examples= [
    {"input": "2+2", "output":"4"},
    {"input": "2+3", "output": "5"},
]
# Next assembling them into few shot prompt template 
example_prompt=ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)
few_shot_prompt=FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples
)
print(few_shot_prompt.format())

# Finally assembling the final prompt and using it with a model 
final_prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math"), 
        few_shot_prompt, 
        ("human", "{input}"),
    ]
)

print("Final Prompt: \n", final_prompt)
formattedChatPrompt=final_prompt.format_messages(
    input="What's the square of a triangle?"
)
print("Formatted Chat Prompt: \n", formattedChatPrompt)
chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

response=chat.invoke(formattedChatPrompt)
print("\n", response)
# from langchain_community.chat_models import ChatAnthropic

# chain=final_prompt | ChatAnthropic(temperature=0)
# chain.invoke({"input":"what's the square of the Triangle?"})
# Providing examples makes the model more intelligent 