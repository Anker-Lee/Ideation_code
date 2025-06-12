from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any
from ..chains.ideation_chain import IdeationChain
from ..schemas.ideation import IdeationRequest, IdeationResponse
from ..utils.logger import get_logger

# 获取日志记录器
logger = get_logger(__name__)

router = APIRouter()
ideation_chain = IdeationChain()

@router.post("/api/ideation", response_model=IdeationResponse)
async def generate_ideation(request: IdeationRequest) -> Dict[str, Any]:
    """
    生成创意
    
    Args:
        request: 包含主题的请求体
        
    Returns:
        Dict[str, Any]: 包含生成结果的响应
    """
    logger.info(f"收到创意生成请求: topic={request.topic}, context={request.context}")
    
    try:
        result = await ideation_chain.run(
            topic=request.topic,
            context=request.context
        )
        
        logger.info(f"创意生成成功: {result}")
        return IdeationResponse(
            success=True,
            data=result
        )
    except Exception as e:
        logger.error(f"创意生成失败: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/api/ideation/feedback", response_model=IdeationResponse)
async def generate_ideation_with_feedback(
    request: IdeationRequest = Body(...),
    feedback: str = Body(..., embed=True)
) -> Dict[str, Any]:
    """
    根据反馈生成新的创意
    
    Args:
        request: 包含主题的请求体
        feedback: 用户反馈
        
    Returns:
        Dict[str, Any]: 包含生成结果的响应
    """
    logger.info(f"收到带反馈的创意生成请求: topic={request.topic}, feedback={feedback}")
    
    try:
        result = await ideation_chain.run_with_feedback(
            topic=request.topic,
            feedback=feedback,
            context=request.context
        )
        logger.info(f"带反馈的创意生成成功: {result}")
        return IdeationResponse(
            success=True,
            data=result
        )
    except Exception as e:
        logger.error(f"带反馈的创意生成失败: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 