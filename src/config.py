class Config:
    # 密钥，用于保护应用程序的会话和其他安全功能
    SECRET_KEY = 'your_secret_key'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 调试模式（开发环境中使用，生产环境中应设置为 False）
    DEBUG = True

    # 上传文件的保存路径
    UPLOAD_FOLDER = 'uploads'

    # 其他配置选项...
