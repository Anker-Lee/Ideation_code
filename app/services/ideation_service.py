from app.chains.ideation_chain import run_ideation_chain
from app.utils.logger import get_logger

# 获取日志记录器
logger = get_logger(__name__)

def run_ideation_pipeline(topic: str) -> dict:
    """
    运行创意生成流程
    
    Args:
        topic: 用户输入的主题
        
    Returns:
        dict: 包含隐喻和图表设计的字典
    """
    logger.info(f"开始处理主题: {topic}")
    try:
        # 使用链运行创意生成
        result = run_ideation_chain(topic)
        logger.info(f"创意生成完成: {result}")
        return result
    except Exception as e:
        logger.error(f"创意生成失败: {str(e)}", exc_info=True)
        raise Exception(str(e))