from fastapi import APIRouter
from typing import Dict

router = APIRouter()

@router.get("/health")
async def health_check() -> Dict[str, str]:
    """健康检查接口"""
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

@router.get("/version")
async def version_info() -> Dict[str, str]:
    """版本信息接口"""
    return {
        "name": "隐喻数据可视化创意生成系统",
        "version": "1.0.0",
        "description": "基于 LangChain 的多智能体系统"
    } 