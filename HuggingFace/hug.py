import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('HUGGING_FACE_API_KEY')
from langchain_community.llms import HuggingFaceEndpoint

from langchain.prompts import PromptTemplate

# ENDPOINT_URL = "<YOUR_ENDPOINT_URL_HERE>"
# llm = HuggingFaceEndpoint(
#     endpoint_url=ENDPOINT_URL,
#     task="text-generation",
#     model_kwargs={
#         "max_new_tokens": 512,
#         "top_k": 50,
#         "temperature": 0.1,
#         "repetition_penalty": 1.03,
#     },
# )

template="<s>[INST] Write long answer of </s>{question} [/INST]"
print(template)
prompt_template = PromptTemplate.from_template(template)
formatted_prompt_template = prompt_template.format(
    question="IRON movie film?" 

)

repo_id="mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=SECRET_KEY)
# response = llm.invoke(formatted_prompt_template)
# print(response)

# Streaming 
response = llm.stream(formatted_prompt_template)
for res in response:
    print(res, end="", flush=True)
