from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def get_chart_chain():
    # 初始化 LLM
    llm = ChatOpenAI(
        temperature=0.7,
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://ai-yyds.com/v1")
    )
    
    # 定义提示模板
    prompt = PromptTemplate(
        input_variables=["metaphor"],
        template="""
你是一位数据可视化设计专家，善于根据隐喻提出图形构想。

请根据以下隐喻，提出一个或多个图表设计建议，包括图表类型和设计逻辑：

隐喻：{metaphor}
"""
    )
    
    # 创建输出解析器
    output_parser = StrOutputParser()
    
    # 返回处理链
    return prompt | llm | output_parser 