# 隐喻数据可视化创意生成系统

基于 LangChain 的多智能体系统，用于生成数据可视化的创意隐喻和图表设计。

## 功能特点

- 基于主题生成生动的隐喻
- 根据隐喻设计数据可视化方案
- RESTful API 接口
- 前后端分离架构

## 技术栈

- Python 3.9+
- FastAPI
- LangChain
- OpenAI API

## 安装

1. 克隆仓库：
```bash
git clone [repository_url]
cd metaphor_vis_backend
```

2. 创建并激活虚拟环境：
```bash
conda create -n metaphor-vis-env python=3.9
conda activate metaphor-vis-env
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
创建 `.env` 文件并添加以下内容：
```
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://ai-yyds.com/v1
```

## 运行

启动开发服务器：
```bash
uvicorn app.main:app --reload
```

服务器将在 http://localhost:8000 运行

## API 文档

启动服务器后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 主要端点

- `POST /api/ideation`: 生成创意
  - 请求体: `{"topic": "你的主题"}`
  - 返回: 包含隐喻和图表设计的 JSON

## 项目结构

```
📦 metaphor_vis_backend/
├── app/                    # 后端主逻辑模块
│   ├── agents/            # 所有 Agent 定义
│   ├── chains/            # 处理链定义
│   ├── services/          # 接口逻辑
│   ├── utils/             # 工具函数
│   ├── __init__.py        # 包初始化文件
│   └── main.py           # FastAPI 主入口
├── logs/                  # 日志文件目录
├── requirements.txt       # 依赖库列表
├── metaphor_vis_ideation.py  # 主程序入口
├── README.md
└── .env
```

## 开发

- 使用 `black` 进行代码格式化
- 使用 `pylint` 进行代码检查
- 遵循 PEP 8 编码规范

## 许可证

MIT 