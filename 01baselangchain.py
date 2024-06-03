'''
@Description: 
@Author: Panbo Hey
@Date: 2024-06-03 11:49:35
@LastEditTime: 2024-06-03 11:49:59
@LastEditors: Panbo Hey
'''
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

res = chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
print(res)
rescp = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
print("*"*80)
print(rescp)


#---------------------------
# from langchain.prompts import PromptTemplate
# userquestion="这里不重要"
# userquestion_getkey="A空调投诉问题"
# res =  prompt = PromptTemplate.from_template("尊敬的用户您好，感谢你的询问，基于你的问题，请问您询问的是否是关于 {product}?")
# resf = prompt.format(product=userquestion_getkey)
# print(res)
# print(resf)
