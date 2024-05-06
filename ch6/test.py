import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI, OpenAI

chat=ChatOpenAI(model="gpt-3.5-Turbo-0125", api_key=SECRET_KEY)

# Example-1 Text File 
from langchain_community.document_loaders import (CSVLoader, PyPDFLoader,
                                                  TextLoader)

loader = TextLoader("./data/sample.txt")
mydata = loader.load()
# print(mydata)
# print("My Metadata:", mydata[0].metadata)
# print("My Metadata:", mydata[0].metadata.source)

loader = CSVLoader(file_path="./data/NIFTY 50-03-05-2023-to-03-05-2024 - Copy.csv")
data_csv=loader.load()
# print(data_csv)

loader = PyPDFLoader("./data/Resume.SDE.Final.FarhadDubey.pdf")
pages=loader.load_and_split()
pages[0]
print(pages[0])


