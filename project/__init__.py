from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from config import configs
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_wtf.csrf import generate_csrf


db = SQLAlchemy()
redis_db = None


def create_app(config_name):

    create_log(config_name)

    app = Flask(__name__)

    app.config.from_object(configs[config_name])

    db.init_app(app)

    global redis_db
    redis_db = StrictRedis(configs[config_name].REDIS_HOST, configs[config_name].REDIS_PORT)

    # 注册路由
    from project.modules.admin import admin_blueprint
    app.register_blueprint(admin_blueprint)
    from project.modules.homepage import homepage_blueprint
    app.register_blueprint(homepage_blueprint)

    @app.after_request
    def after_request(response):
        csrf = generate_csrf(configs[config_name].SECRET_KEY)
        response.set_cookie("csrf_token", csrf)
        return response

    from project.modules.utils import filter_customer
    app.add_template_filter(filter_customer.filter_css)
    app.add_template_filter(filter_customer.filter_input_type)
    app.add_template_filter(filter_customer.filter_user_css)

    CSRFProtect(app)

    Session(app)

    return app


# logs config
def create_log(config_name):
    import logging
    from logging.handlers import RotatingFileHandler

    # 设置日志的记录等级
    logging.basicConfig(level=configs[config_name].LOGGING_DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
