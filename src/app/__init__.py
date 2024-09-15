from flask import Flask, render_template
app = Flask(__name__)

# 捕获其他 HTTP 错误
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('404.html'), 404

# 导入配置
from config import Config
app.config.from_object(Config)

# 导入蓝图并注册
from app.views import toolbox
app.register_blueprint(toolbox.bp)