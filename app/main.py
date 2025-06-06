from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.ideation_api import router as ideation_router
from .services.healthcheck import router as healthcheck_router
from .utils.logger import get_logger

# 获取日志记录器
logger = get_logger(__name__)

app = FastAPI(
    title="隐喻数据可视化创意生成系统",
    description="基于 LangChain 的多智能体系统，用于生成数据可视化的创意隐喻和图表设计",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(ideation_router)
app.include_router(healthcheck_router)

@app.get("/")
async def root():
    """根路径"""
    logger.info("访问根路径")
    return {
        "message": "欢迎使用隐喻数据可视化创意生成系统",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

@app.on_event("startup")
async def startup_event():
    """应用启动时的初始化操作"""
    logger.info("应用启动")
    
@app.on_event("shutdown")
async def shutdown_event():
    """应用关闭时的清理操作"""
    logger.info("应用关闭") 