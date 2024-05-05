# Useful when unaware of what role should i use message template   
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    MessagesPlaceholder)

human_prompt="Summarize our conversation so far in {word_count} words."
human_message_prompt=HumanMessagePromptTemplate.from_template(human_prompt) 

chat_prompt=ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)


from langchain_core.messages import AIMessage, HumanMessage

human_message=HumanMessage(content="What's the best way to learn Programming?")
ai_message=AIMessage(
    content="""
            1.Chose a programming language that your decide to learn .
            2. Start with the basice. Familiarize with the basics & then move forward towards tough concept.
            3. Practice prictice, practice. 
"""
)
chat_prompt.format_prompt(
    conversation=[human_message, ai_message], word_count="10"
).to_messages() 