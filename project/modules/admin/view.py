from . import admin_blueprint
from project.modules.models import User


from flask import render_template, request, jsonify, current_app
from flask import redirect, url_for, session, g

from project.modules.utils.pack import save_pic

from project import db
import datetime


@admin_blueprint.route("/index", methods=["GET"])
@save_pic
def index():

    return render_template("admin/admin_index.html", pic_urls=g.pic_list)


@admin_blueprint.route("/login", methods=["POST"])
def login():
    # print(request.form, request.values)
    name = request.form.get("input_name")

    pwd = request.form.get("input_pwd")

    index_back = request.form.get("index_back")

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
    session["user_id"] = user.id

    return jsonify(error=200, errmsg="登录成功", back=index_back)


@admin_blueprint.route("/page", methods=["GET"])
@save_pic
def page():
    name = session.get('nick_name')

    user_id = session.get("user_id")

    index_back = request.args.get("index", 1)

    try:
        index_num = int(index_back)
    except Exception as e:
        return jsonify(error=1002, errmsg="缺少参数")

    if not name:
        return redirect(url_for("admin.index"))

    try:
        users = User.query.filter(User.id_style == "user").all()
    except Exception as e:
        return jsonify(error=1403, errmsg="数据库查询错误")

    u_list = []
    if users:
        for u in [user for user in users]:
            u_list.append(u.to_user_dict())

    print(index_num)

    data = {
        "user_id": user_id,
        "user_name": name,
        "tabs": ["用户信息", "旅游景点", "攻略", "问题", "", "", "", "", "".join([name, " ", "退出"])],
        "index_back": g.pic_list[index_num] if index_back else g.pic_list[0],
        "users": u_list if users else None,
    }

    return render_template("admin/admin_page.html", data=data)


@admin_blueprint.route("/get_admin_info", methods=["GET"])
def admin_info():

    admin_id = request.args.get("admin_id")

    if not id:
        return jsonify(error=1044, errmsg="用户ID为空")

    try:
        admin = User.query.get(admin_id)
        users = User.query.filter(User.id_style == "user").all()
    except Exception as e:
        return jsonify(error=1403, errmsg="数据库查询错误")

    if not admin:
        return jsonify(error=1619, errmsg="用户不存在")

    data = {
        "admin": admin.to_admin_dict() if admin else None,
        # "users": users
    }

    return jsonify(error=200, errmsg="成功", data=data)


@admin_blueprint.route("/logout", methods=["GET"])
def logout():
    user_id = session.get("user_id")
    session.pop("nick_name")
    session.pop("user_id")

    if not user_id:
        return jsonify(error=1421, errmsg="参数错误")

    if session.get("user_id"):
        return jsonify(error=1400, errmsg="退出错误")

    try:
        admin = User.query.get(user_id)
    except Exception as e:
        return jsonify(error=1420, errmsg="查询错误")

    admin.last_login = datetime.datetime.now()

    try: 
        db.session.commit()
    except Exception as e:
        return jsonify(error=1410, errmsg="错误")

    return redirect(url_for("admin.index"))


@admin_blueprint.route("/get_user_info", methods=["GET"])
def get_user_info():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify(error=1404, errmsg="用户未查询到")

    try:
        user = User.query.get(user_id)
    except Exception as e:
        return jsonify(error=1400, errmsg="信息查询错误")

    data = {
        "user": user.to_user_dict(),
    }
    return jsonify(error=200, data=data)


# 改头像
@admin_blueprint.route("/alter_pic/", methods=["POST", "GET"])
def alter_pic():
    user_id = request.form.get("i")

    file_pic = request.files.get("pic_url")

    print(user_id, type(file_pic))

    if not all([user_id, file_pic]):
        return jsonify(error=1004, errmsg="参数错误")

    try:
        file_bin = file_pic.read()
    except Exception as e:
        return jsonify(error=1003, errmsg="文件无法读取")

    import time
    import os

    time_now = time.time()
    cur_prj = os.getcwd()
    with open(''.join((cur_prj, "/project/static/user_head_pic/user{}.jpg".format(time_now))), "wb") as f:
        f.write(file_bin)

    # 保存至数据库
    try:
        user = User.query.get(user_id)
    except Exception as e:
        return jsonify(error=1400, errmsg="用户信息错误")

    if not user:
        return jsonify(error=1004, errmsg="用户信息为空")

    user.pic_url = "../static/user_head_pic/user{}.jpg".format(time_now)

    try:
        db.session.commit()
    except Exception as e:
        return jsonify(error=1004, errmsg="修改错误")

    data = {
        "pic_url": user.pic_url,
    }

    return jsonify(error=200, errmsg="success", data=data)



@admin_blueprint.route("/alter_user_info/", methods=["POST"])
def alter_user_info():

    nick_name = request.form.get("nick")

    sign = request.form.get("sign")

    sex = request.form.get("sex_info")

    phone = request.form.get("phone")

    live = request.form.get("live")

    u_id = request.form.get("i")

    if not all([nick_name, sign, sex, phone, live]):
        return jsonify(error=1200, errmsg="参数错误")

    print(nick_name, sex, sign)

    try:
        user = User.query.get(u_id)
    except Exception as e:
        return jsonify(errmsg="查询错误", error=1400)

    user.nick_name = nick_name
    user.sex = sex
    user.phone_num = phone
    user.user_live = live
    user.private_sign = sign
    # import datetime
    # user.last_login = datetime.datetime.now()

    try: 
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(error=1430, errmsg="更新数据错误")

    data = {
        "user": user.to_user_dict(),
    }

    return jsonify(error=200, errmsg="成功", data=data)
