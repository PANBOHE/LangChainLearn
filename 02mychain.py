'''
@Description: 
@Author: Panbo Hey
@Date: 2024-06-03 11:50:05
@LastEditTime: 2024-06-03 11:50:28
@LastEditors: Panbo Hey
'''
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import os
import time
os.environ["OPENAI_API_KEY"] = "your_api_key"

class CommaSeparatedListOutputParser(BaseOutputParser):
    """将 LLM 调用的输出解析为逗号分隔的列表。"""

    def parse(self, text: str):
        """解析 LLM 调用的输出。"""
        #print text.strip().split(", ")
        return text

template = "您是一位有用的助手，可以生成逗号分隔的列表。用户将传入一个类别，您应该在该类别中生成 5 个对象，并以逗号分隔列表形式。仅返回逗号分隔的列表，仅此而已。"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
start_time = time.time()
chain = LLMChain(
    llm = ChatOpenAI(),
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser()
)
res = chain.run("colors")
print(res)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"代码运行时间: {elapsed_time:.2f} 秒")