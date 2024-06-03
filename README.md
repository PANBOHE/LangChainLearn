<!--
 * @Description: 
 * @Author: Panbo Hey
 * @Date: 2024-06-03 11:49:17
 * @LastEditTime: 2024-06-03 16:32:25
 * @LastEditors: Panbo Hey
-->
# LangChainLearn
 2024年6月3日学习LangChain

 ###细节描述：https://zhuanlan.zhihu.com/p/701300258

## Model I/O
- Prompts 提示词
  - Template 模板+复用
    - 子节点1.1
    - 子节点1.2
  - Selector 提示词选择器
    - 根据不同的条件选择不同的提示词：意图分析、实体识别、槽位填充、槽位约束
- Language Models 语言模型
  - LLM
    - 生成模型
  - Chat
    - 对话形态：chatbot
  -不同的语言模型：chatglm3-6b，llama3-8b
- Output Parsers
  - 输出解析器
    - 解析模型输出，生成结果
    - JSON
    - Structured

## Data Connection
本地私有数据库使用
- Vector Stores 向量存储
  - Enbedding
    - 文本嵌入语言模型
    - 向量存储，向量嵌入
    - 不同的embedding模型：bert-base-chinese，gpt2-medium，xlnet-base-cased
  - Memory、Index、Search
    - 不同的响亮数据库：faiss，milvus，annoy,chroma
    - 可以存在内存里，也可以存在自建数据库，也可以放在云端。
  - 映射表
- Document Loaders 文档加载器
  - 文档加载器
    - 加载文档数据，进行预处理
    - 不同的数据源：本地文件，网络数据，数据库数据（Folder/File/Web）
    - 预处理：分词，去停用词，去重，分句，词性标注，实体识别，槽位填充，槽位约束等。
- Document Transforms 文档转换器/Splitters 文档分割器
  - text
  - code
  - Token
- Document Retrievers 文档检索器
  - User Input Query
  - Vector DB
    - 通过向量数据库的能力进行向量的匹配、近似度的匹配，获取相关文档的内容
  - Web API
    - 通过Web API进行文档的检索，获取相关文档的内容
  - 其他

## Memory
历史记录，可以实现多轮对话与精准分析
- Buffer
  - 即存即用
- Vector DB
  - 向量数据库/本地可以保存
- KV DB
- SQL DB

## Chains
串联Model I/O、Data Connections、Memory，组合链
- Foundational LLM
  - 基础语言模型
  - 把模型+Memory串联起来，形成一个完整的语言模型
- Dialogue Models
  - 对话模型
  - Conversational QA 串联起来，形成一个完整的对话模型
- Retrieval QA Models
  - 将数据库和model串联起来，形成一个完整的检索QA模型
- Document
  - 基于本地数据文档信息获取
- Sequence
  - 基于序列信息获取

## Agents+tools
- 基于Model I/O、Data Connections、Memory、Chains，形成Agent
- Executors(Chains)
  - ReAct(Reason-Act)
  - Plan-Execute-Act
  - 基于Chains，形成Agent
  - OpenAI GPT-3:唯一真神

## Callback
LangChain提供了回调能力，做日志记录、调用链路的追踪
- LangSmith
  - 语言模型训练工具
  - 训练过程的日志记录
  - 调用链路的追踪
- 其他
