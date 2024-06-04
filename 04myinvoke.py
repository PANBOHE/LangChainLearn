'''
@Description: 
@Author: Panbo Hey
@Date: 2024-06-04 10:28:43
@LastEditTime: 2024-06-04 10:28:53
@LastEditors: Panbo Hey
'''
# Without LCEL
from typing import List
import openai
import os 
os.environ["OPENAI_API_KEY"] = "my_api_key"

prompt_template = "Tell me a short joke about {topic}"
client = openai.OpenAI()

def call_chat_model(messages: List[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=messages,
    )
    return response.choices[0].message.content

def invoke_chain(topic: str) -> str:
    prompt_value = prompt_template.format(topic=topic)
    messages = [{"role": "user", "content": prompt_value}]
    return call_chat_model(messages)

res = invoke_chain("ice cream")
print(res)

# LCEL
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = ({"topic": RunnablePassthrough()} | prompt | model | output_parser)
chain.invoke("ice cream")
