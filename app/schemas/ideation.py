"""
定义创意生成请求和响应模型，以及隐喻生成输入和输出模型，图表设计输入和输出模型。

创意生成请求和响应模型：
- IdeationRequest：创意生成请求模型
- IdeationFeedbackRequest：带反馈的创意生成请求模型
- IdeationResponse：创意生成响应模型

隐喻生成输入和输出模型：

"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel

class IdeationRequest(BaseModel):
    """创意生成请求模型"""
    topic: str
    context: Optional[Dict[str, Any]] = None

class IdeationFeedbackRequest(BaseModel):
    """带反馈的创意生成请求模型"""
    request: IdeationRequest
    feedback: str

class GenerationHistory(BaseModel):
    """生成历史记录"""
    generation_count: int
    result: str
    metadata: Dict[str, Any]

class IdeationResponse(BaseModel):
    """创意生成响应模型"""
    success: bool
    data: Dict[str, Any]
    session_id: Optional[str] = None
    generation_count: Optional[int] = None
    error: Optional[str] = None

class MetaphorInput(BaseModel):
    """隐喻生成输入模型"""
    topic: str
    context: Optional[Dict[str, Any]] = None

class MetaphorOutput(BaseModel):
    """隐喻生成输出模型"""
    metaphor: str
    explanation: str
    metadata: Optional[Dict[str, Any]] = None

class ChartInput(BaseModel):
    """图表设计输入模型"""
    metaphor: str
    topic: str
    context: Optional[Dict[str, Any]] = None

class ChartOutput(BaseModel):
    """图表设计输出模型"""
    chart_type: str
    design_description: str
    metadata: Optional[Dict[str, Any]] = None 