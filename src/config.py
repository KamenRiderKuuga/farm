from app.loader.tools_loader import load_tools


class Config:
    # 调试模式（开发环境中使用，生产环境中应设置为 False）
    DEBUG = True

    # 其他配置选项...
    TOOLS = load_tools()
