from typing import Dict, Any
from ...agents.base import AgentBase, AgentInput, AgentOutput

class ScamperAgentBase(AgentBase):
    """SCAMPER Agent 基类"""
    
    def __init__(self, name: str):
        super().__init__(name=f"scamper_{name}")
        self.operation_type = name.upper()
    
    async def validate(self, input_data: AgentInput) -> bool:
        """验证输入数据"""
        return bool(input_data.topic and len(input_data.topic.strip()) > 0)
    
    async def run(self, input_data: AgentInput) -> AgentOutput:
        """运行 SCAMPER 操作"""
        if not await self.validate(input_data):
            raise ValueError("Invalid input data")
        
        result = await self._apply_scamper_operation(input_data)
        return AgentOutput(
            result=result,
            metadata={"operation_type": self.operation_type}
        )
    
    async def _apply_scamper_operation(self, input_data: AgentInput) -> str:
        """应用具体的 SCAMPER 操作"""
        raise NotImplementedError("Subclasses must implement _apply_scamper_operation") 