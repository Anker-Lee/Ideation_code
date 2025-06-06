from typing import List, Dict, Any
from .base import AgentBase, AgentInput, AgentOutput
from ..utils.logger import get_logger

# 获取日志记录器
logger = get_logger(__name__)

class BlueHatAgent(AgentBase):
    """蓝帽 Agent：负责整个 ideation 流程的控制和协调"""
    
    def __init__(self):
        super().__init__(name="blue_hat")
        self.agents = {}  # 存储其他 Agent 实例
        logger.info("初始化蓝帽 Agent")
    
    async def register_agent(self, agent: AgentBase):
        """注册其他 Agent"""
        self.agents[agent.name] = agent
        logger.info(f"注册 Agent: {agent.name}")
    
    async def validate(self, input_data: AgentInput) -> bool:
        """验证输入数据"""
        is_valid = bool(input_data.topic and len(input_data.topic.strip()) > 0)
        logger.debug(f"输入验证结果: {is_valid}")
        return is_valid
    
    async def run(self, input_data: AgentInput) -> AgentOutput:
        """运行整个 ideation 流程"""
        logger.info(f"开始运行 ideation 流程: topic={input_data.topic}")
        
        if not await self.validate(input_data):
            logger.error("输入数据验证失败")
            raise ValueError("Invalid input data")
        
        try:
            # 1. 生成阶段
            logger.info("开始生成阶段")
            preinventive_results = await self._run_generation_phase(input_data)
            logger.info(f"生成阶段完成: {preinventive_results}")
            
            # 2. 探索阶段
            logger.info("开始探索阶段")
            exploration_results = await self._run_exploration_phase(preinventive_results)
            logger.info(f"探索阶段完成: {exploration_results}")
            
            # 3. 再生成阶段（如果需要）
            logger.info("开始再生成阶段")
            final_results = await self._run_regeneration_phase(exploration_results)
            logger.info(f"再生成阶段完成: {final_results}")
            
            # 将结果转换为字符串
            result_str = str(final_results) if final_results else "暂无结果"
            
            return AgentOutput(
                result=result_str,
                metadata={
                    "phase_results": {
                        "generation": preinventive_results,
                        "exploration": exploration_results
                    }
                }
            )
        except Exception as e:
            logger.error(f"ideation 流程执行失败: {str(e)}", exc_info=True)
            raise
    
    async def _run_generation_phase(self, input_data: AgentInput) -> Dict[str, Any]:
        """运行生成阶段"""
        logger.debug("运行生成阶段")
        # TODO: 实现生成阶段逻辑
        return {"status": "生成阶段完成"}
    
    async def _run_exploration_phase(self, generation_results: Dict[str, Any]) -> Dict[str, Any]:
        """运行探索阶段"""
        logger.debug("运行探索阶段")
        # TODO: 实现探索阶段逻辑
        return {"status": "探索阶段完成"}
    
    async def _run_regeneration_phase(self, exploration_results: Dict[str, Any]) -> Dict[str, Any]:
        """运行再生成阶段"""
        logger.debug("运行再生成阶段")
        # TODO: 实现再生成阶段逻辑
        return {"status": "再生成阶段完成"} 