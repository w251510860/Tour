from . import admin_blueprint
from project.modules.models import User


from flask import render_template, request, jsonify, current_app, redirect, url_for, session


@admin_blueprint.route("/index", methods=["GET"])
def index():
    pic_list = [
        "../static/picture/admin_index.jpg",
        "../static/picture/admin_index1.jpg",
        "../static/picture/admin_index2.jpg",
        "../static/picture/admin_index3.jpg",
        "../static/picture/admin_index4.jpg",
    ]
    return render_template("admin_index.html", pic_urls=pic_list)


@admin_blueprint.route("/login", methods=["POST"])
def login():
    # print(request.form, request.values)
    name = request.form.get("input_name")

    pwd = request.form.get("input_pwd")

    try:
        user = User.query.filter(User.nick_name == name).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=1040, errmsg="数据库查询错误")

    if not user:
        return jsonify(error=1404, errmsg="管理员不存在")

    if not (user.password == pwd):
        return jsonify(error=1405, errmsg="用户密码填写错误")

    session["nick_name"] = user.nick_name

    return jsonify(error=200, errmsg="登录成功")


@admin_blueprint.route("/page", methods=["GET"])
def page():
    name = session.get('nick_name')

    if not name:
        return redirect(url_for("admin.index"))

    return "page is ok".join(name)
