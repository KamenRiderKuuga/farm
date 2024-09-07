from flask import Flask
app = Flask(__name__)

# 导入配置
from config import Config
app.config.from_object(Config)

# 导入蓝图并注册
from app.views import toolbox
app.register_blueprint(toolbox.bp)