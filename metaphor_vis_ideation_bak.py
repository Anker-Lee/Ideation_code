# 导入必要的库
import os
import openai
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 设置 OpenAI API 密钥和基础URL
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_base_url = os.getenv("OPENAI_BASE_URL", "https://ai-yyds.com/v1")

if not openai_api_key:
    raise ValueError("请设置 OPENAI_API_KEY 环境变量")

# 定义隐喻生成的 prompt
metaphor_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
你是一位隐喻专家。请为下列主题构思一个生动、具体的隐喻：

主题：{topic}
请用一句话描述这个隐喻。
"""
)

# 定义图表构思的 prompt
chart_prompt = PromptTemplate(
    input_variables=["metaphor"],
    template="""
你是一位数据可视化设计专家，善于根据隐喻提出图形构想。

请根据以下隐喻，提出一个或多个图表设计建议，包括图表类型和设计逻辑：

隐喻：{metaphor}
"""
)

# 初始化 OpenAI LLM（使用 GPT-4 模型和自定义基础URL）
llm = ChatOpenAI(
    temperature=0.7, 
    model="gpt-4o-mini", 
    openai_api_key=openai_api_key,
    base_url=openai_base_url
)

# 创建输出解析器
output_parser = StrOutputParser()

# 创建两个链条
metaphor_chain = metaphor_prompt | llm | output_parser
chart_chain = chart_prompt | llm | output_parser

# 主程序入口
def main():
    try:
        print("欢迎使用隐喻数据可视化 Ideation 系统！")
        topic = input("请输入你的主题或数据集描述：")
        
        # 运行第一个链条，生成隐喻
        print("\n🔮 正在生成隐喻...")
        metaphor = metaphor_chain.invoke({"topic": topic})
        print(f"生成的隐喻：{metaphor}")
        
        # 运行第二个链条，生成图表构思
        print("\n🎨 正在生成图表设计...")
        chart_idea = chart_chain.invoke({"metaphor": metaphor})
        
        # 输出结果
        print("\n🧠 最终输出结果：")
        print(chart_idea)
    except Exception as e:
        print(f"\n❌ 发生错误：{str(e)}")

if __name__ == "__main__":
    main()
