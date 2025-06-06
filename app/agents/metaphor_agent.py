from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def get_metaphor_chain():
    # 初始化 LLM
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://ai-yyds.com/v1")
    )
    
    # 定义提示模板
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
你是一位隐喻专家。请为下列主题构思一个生动、具体的隐喻：

主题：{topic}
请用一句话描述这个隐喻。
"""
    )
    
    # 创建输出解析器
    output_parser = StrOutputParser()
    
    # 返回处理链
    return prompt | llm | output_parser 