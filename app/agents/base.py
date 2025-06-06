from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel

class AgentInput(BaseModel):
    """Agent 输入基类"""
    topic: str
    context: Dict[str, Any] = {}

class AgentOutput(BaseModel):
    """Agent 输出基类"""
    result: str
    metadata: Dict[str, Any] = {}

class AgentBase(ABC):
    """Agent 基类，定义基本接口"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    async def run(self, input_data: AgentInput) -> AgentOutput:
        """运行 Agent 的主要逻辑"""
        pass
    
    @abstractmethod
    async def validate(self, input_data: AgentInput) -> bool:
        """验证输入数据是否有效"""
        pass 