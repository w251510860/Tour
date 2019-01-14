from . import admin_blueprint
from project.modules.models import User, Travel, Blog


from flask import render_template, request, jsonify, current_app
from flask import redirect, url_for, session, g

from project.modules.utils.pack import save_pic

from project import db
import datetime
import time


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

    user_style = user.id_style

    if user_style not in ['user', 'admin']:
        return jsonify(error=1405, errmsg='游客未注册')

    session["nick_name"] = user.nick_name
    session["user_id"] = user.id

    return jsonify(error=200, errmsg="登录成功", back=index_back, style=user_style)


@admin_blueprint.route("/page/<int:type>", methods=["GET"])
@save_pic
def page(type):
    name = session.get('nick_name')

    user_id = session.get("user_id")

    index_back = request.args.get("index", 1)

    try:
        index_num = int(index_back)
    except Exception:
        return jsonify(error=1002, errmsg="缺少参数")

    if not name:
        return redirect(url_for("admin.index"))

    try:
        users = User.query.filter(User.id_style == "user").all()
    except Exception:
        return jsonify(error=1403, errmsg="数据库查询错误")

    u_list = []
    if users:
        for u in [user for user in users]:
            u_list.append(u.to_user_dict())

    data = {
        "user_id": user_id,
        "user_name": name,
        "tabs": ["用户信息", "旅游景点", "攻略", "问题", "", "", "", "", "".join([name, " ", "退出"])],
        "index_back": g.pic_list[index_num] if index_back else g.pic_list[0],
        "users": u_list if users else None,
    }

    return render_template("admin/admin_page.html", data=data, type=type)


@admin_blueprint.route("/get_admin_info", methods=["GET"])
def admin_info():

    admin_id = request.args.get("admin_id")

    if not id:
        return jsonify(error=1044, errmsg="用户ID为空")

    try:
        admin = User.query.get(admin_id)
        users = User.query.filter(User.id_style == "user").all()
    except Exception:
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
    except Exception:
        return jsonify(error=1420, errmsg="查询错误")

    admin.last_login = datetime.datetime.now()

    try:
        db.session.commit()
    except Exception:
        return jsonify(error=1410, errmsg="错误")

    return redirect(url_for("admin.index"))


@admin_blueprint.route("/get_user_info", methods=["GET"])
def get_user_info():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify(error=1404, errmsg="用户未查询到")

    try:
        user = User.query.get(user_id)
    except Exception:
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

    if not all([user_id, file_pic]):
        return jsonify(error=1004, errmsg="参数错误")

    try:
        file_bin = file_pic.read()
    except Exception as e:
        return jsonify(error=1003, errmsg="文件无法读取%s" % e)

    import os

    time_now = time.time()
    cur_prj = os.getcwd()
    with open(''.join((cur_prj,
                       "/project/static/"
                       "user_head_pic/user{}.jpg".
                       format(time_now))),
              "wb") as f:
        f.write(file_bin)

    # 保存至数据库
    try:
        user = User.query.get(user_id)
    except Exception as e:
        return jsonify(error=1400, errmsg="用户信息错误 %s" % e)

    if not user:
        return jsonify(error=1004, errmsg="用户信息为空")

    user.pic_url = "../../static/user_head_pic/user{}.jpg".format(time_now)

    try:
        db.session.commit()
    except Exception as e:
        return jsonify(error=1004, errmsg="修改错误 %s" % e)

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
        return jsonify(errmsg="查询错误%s" % e, error=1400)

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


@admin_blueprint.route('/travel', methods=['GET'])
def travel():
    if request.method == 'GET':

        travel_obj = Travel.query.all()

        data = {
            'travel': [t.to_dict() for t in travel_obj],
        }

        return render_template('admin/travel.html', data=data)


@admin_blueprint.route('/travel/<int:pk>', methods=['GET'])
def travel_pk(pk):
    if request.method == 'GET':

        try:
            travel_obj = Travel.query.get(pk)
        except Exception:
            return jsonify(status=404, data={'msg': '该旅游信息不存在'})

        return render_template('admin/add_travel.html',
                               data=travel_obj.to_dict())


@admin_blueprint.route("/add_travel", methods=['GET', 'POST'])
def add_travel():

    if request.method == 'GET':

        return render_template('admin/add_travel.html')

    else:
        name = request.form.get('name')
        pic_link = request.form.get('pic_link')
        open_time = request.form.get('open_time')
        advice_time = request.form.get('advice_time')
        phone = request.form.get('phone')
        price = request.form.get('price')
        website = request.form.get('website')
        place = request.form.get('place')

        data = {
            'name': name,
            'pic_link': pic_link,
            'open_time': open_time,
            'advice_time': advice_time,
            'phone': phone,
            'price': price,
            'website': website,
            'place': place,
        }
        travel = Travel(**data)
        db.session.add(travel)
        db.session.commit()
        return jsonify(data=travel.to_dict())


@admin_blueprint.route('/delete_travel/<int:pk>', methods=['GET'])
def delete_travel(pk):
    try:
        t = Travel.query.get(pk)
    except Exception:
        return jsonify(status=400, data={'msg': '信息已不存在'})
    try:

        db.session.delete(t)
        db.session.commit()
    except Exception:
        return jsonify(status=400, data={'msg': '删除失败'})

    return redirect(url_for("admin.page", type=2))


@admin_blueprint.route('/update_travel/<int:pk>', methods=['POST'])
def update_tavel(pk):
    name = request.form.get('name')
    pic_link = request.form.get('pic_link')
    open_time = request.form.get('open_time')
    advice_time = request.form.get('advice_time')
    phone = request.form.get('phone')
    price = request.form.get('price')
    website = request.form.get('website')
    place = request.form.get('place')

    data = {
        'name': name,
        'pic_link': pic_link,
        'open_time': open_time,
        'advice_time': advice_time,
        'phone': phone,
        'price': price,
        'website': website,
        'place': place,
    }

    travel_num = Travel.query.filter_by(id=pk).update(data)
    if not travel_num:
        return jsonify(data={'msg': '更新错误'}, status=400)

    db.session.commit()

    return jsonify({})


@admin_blueprint.route('/look_blog', methods=['GET'])
def look_blog():

    blog_objects = Blog.query.all()

    data = {
        'blog': [i.to_dict() for i in blog_objects],
    }

    return render_template('admin/look_blog.html', data=data)


@admin_blueprint.route('/delete_blog/<int:pk>', methods=['GET'])
def delete_blog(pk):
    try:
        b = Blog.query.get(pk)
    except Exception:
        return jsonify(status=200, data={'msg': '已删除'})

    try:
        db.session.delete(b)
        db.session.commit()
    except Exception:
        return jsonify(status=400, data={'msg': '删除失败'})

    return redirect(url_for('admin.page', type=3))


@admin_blueprint.route('/update_blog/<int:pk>', methods=['POST'])
def update_blog(pk):
    t = Blog.query.get(pk)
    title = request.form.get('title')
    cnt = request.form.get('content')

    if not t:
        return jsonify(status=400, data={'msg': '信息已不存在'})

    t.title = title
    t.content = cnt

    db.session.commit()
    return jsonify(status=200)
