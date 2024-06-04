'''
@Description: 
@Author: Panbo Hey
@Date: 2024-06-04 11:48:11
@LastEditTime: 2024-06-04 11:48:21
@LastEditors: Panbo Hey
'''
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "your_api_key"

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("start with 'thank you for asking!'")
chain = prompt | model

# 链的输入模式是其第一个部分（prompt）的输入模式。
reschain = chain.input_schema.schema()
print(reschain)

resprompt = prompt.input_schema.schema()
print(resprompt)


resmodel = model.input_schema.schema()
print(resmodel)

# 链的输出模式是其最后一部分的输出模式，本例中是 ChatModel，它输出一个 ChatMessage
resoutput = chain.output_schema.schema()
print(resoutput)

