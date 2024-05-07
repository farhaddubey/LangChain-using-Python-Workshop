
# LangChain provides different types of message prompt template. The most commonly used are AIMessagePromptTemplate, SystemMessagePromptTemplate, 
# HumanMessagePromptTemplate  that creates AIMessage, SystemMessage, HumanMessage respectively 
from langchain_core.prompts import ChatMessagePromptTemplate

prompt = "May the {subject} be with you"
chat_message_prompt=ChatMessagePromptTemplate.from_template(
    role="Jedi", template=prompt 
)
chat_message_prompt.format(subject="force") 
