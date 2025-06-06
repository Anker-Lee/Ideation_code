from typing import List, Dict, Any
from ..agents.base import AgentBase, AgentInput, AgentOutput
from ..agents.blue_hat import BlueHatAgent
from ..utils.logger import get_logger

# 获取日志记录器
logger = get_logger(__name__)

class IdeationChain:
    """主 ideation 链，协调各个 Agent 的工作"""
    
    def __init__(self):
        self.blue_hat = BlueHatAgent()
        self.agents: Dict[str, AgentBase] = {}
        # 存储会话状态
        self.sessions: Dict[str, Dict[str, Any]] = {}
    
    def register_agent(self, agent: AgentBase):
        """注册 Agent"""
        self.agents[agent.name] = agent
        self.blue_hat.register_agent(agent)
    
    def _get_session_id(self, topic: str) -> str:
        """生成会话ID"""
        return f"session_{hash(topic)}"
    
    def _get_session(self, topic: str) -> Dict[str, Any]:
        """获取或创建会话"""
        session_id = self._get_session_id(topic)
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "topic": topic,
                "generation_count": 0,
                "history": []
            }
        return self.sessions[session_id]
    
    async def run(self, topic: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """运行整个 ideation 流程"""
        logger.info(f"开始新的创意生成流程: topic={topic}")
        
        # 获取或创建会话
        session = self._get_session(topic)
        session["generation_count"] += 1
        
        input_data = AgentInput(
            topic=topic,
            context=context or {}
        )
        
        # 通过蓝帽 Agent 协调整个流程
        result = await self.blue_hat.run(input_data)
        
        # 保存到历史记录
        session["history"].append({
            "generation_count": session["generation_count"],
            "result": result.result,
            "metadata": result.metadata
        })
        
        return {
            "result": result.result,
            "metadata": result.metadata,
            "session_id": self._get_session_id(topic),
            "generation_count": session["generation_count"]
        }
    
    async def run_with_feedback(self, topic: str, feedback: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """运行带反馈的 ideation 流程"""
        logger.info(f"开始带反馈的创意生成: topic={topic}, feedback={feedback}")
        
        # 获取会话
        session = self._get_session(topic)
        if not session["history"]:
            logger.warning("没有找到之前的生成记录，将进行新的生成")
            return await self.run(topic, context)
        
        # 获取上一次的结果
        last_result = session["history"][-1]
        
        # 准备新的上下文
        if context is None:
            context = {}
        context.update({
            "feedback": feedback,
            "previous_result": last_result["result"],
            "previous_metadata": last_result["metadata"]
        })
        
        # 运行新的生成
        return await self.run(topic, context)