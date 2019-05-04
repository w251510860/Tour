from flask import Blueprint
# 创建蓝图，并设置蓝图前缀
scenic_blu = Blueprint("scenic", __name__, url_prefix='/scenic')

from . import view