'''
@Description: 
@Author: Panbo Hey
@Date: 2024-06-03 17:49:35
@LastEditTime: 2024-06-03 17:49:44
@LastEditors: Panbo Hey
'''
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"


prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "ice cream"})
