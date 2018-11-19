from flask import g
from functools import wraps


# 装饰器 -- 背景的路径全局变量保存
def save_pic(func):
    @wraps(func)
    def inner(*args, **kwargs):
        pic_list = [
            "../static/picture/admin_index.jpg",
            "../static/picture/admin_index1.jpg",
            "../static/picture/admin_index2.jpg",
            "../static/picture/admin_index3.jpg",
            "../static/picture/admin_index4.jpg",
        ]

        g.pic_list = pic_list

        return func(*args, **kwargs)

    return inner
