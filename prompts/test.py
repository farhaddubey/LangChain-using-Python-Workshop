import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI, OpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

# Example-1 Text File 
from langchain_community.document_loaders import (BSHTMLLoader, CSVLoader,
                                                  PyPDFLoader, TextLoader)

loader = TextLoader("./data/sample.txt")
mydata = loader.load()
# print(mydata)
# print("My Metadata:", mydata[0].metadata)
# print("My Metadata:", mydata[0].metadata.source)

loader = CSVLoader(file_path="./data/NIFTY 50-03-05-2023-to-03-05-2024 - Copy.csv")
data_csv=loader.load()
# print(data_csv)

# loader = PyPDFLoader("./data/Resume.SDE.Final.FarhadDubey.pdf")
# pages=loader.load_and_split()
# pages[0]
# print(pages[0])

# loader = PyPDFLoader("./data/sam")


# USE CASES THAT'S HOW WE CAN MAKE A LEGAL AI ADVISOR  
loader = TextLoader("./data/legal.txt")
my_context=loader.load()[0].page_content
human_template="{question}\n{company_legal_doc}"
chat_prompt=ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(human_template)
])
formatted_chat_prompt=chat_prompt.format_messages(
    question="How can i apply for PAN card? ",
    company_legal_doc=my_context
)
print("Formatted Chat Prompt: ", formatted_chat_prompt)
response=chat.invoke(formatted_chat_prompt)
print("\n", response.content)

