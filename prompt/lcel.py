import os
import dotenv
load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain_core.prompts import PromptTemplate
prompt_template=PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}"
)
prompt_val=prompt_template.invoke({"adjective":"funny", "content":"chickens"})
prompt_val

prompt_val.to_string() 
print(prompt_val.to_string)
print(prompt_val.to_messages())

chat_template=ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a helpful assistant that re-writes the user text to"
                "sound more updbeat"
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
chat_val=chat_template.invoke({"text":"I dont like eating tasty things."})
chat_val.to_messages()
print(chat_val.to_string())
