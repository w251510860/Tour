import time

from flask import render_template, request, current_app, jsonify, session, redirect, url_for

from project import db
from . import user_blueprint
from project.modules.models import User


@user_blueprint.route('/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        user = User.query.filter(User.nick_name == username).first()
    except Exception as e:
        current_app.log.error(e)
        return jsonify(error=4004, errmsg='用户不存在')
    if password != user.password:
        return jsonify(error=4005, errmsg='用户名或密码错误')
    session['username'] = username
    session['user_id'] = user.id
    # data = {
    #     'user': user.to_user_dict() if user else None
    # }
    return jsonify('登录成功', 200)


@user_blueprint.route('/logout', methods=['get'])
def logout():
    username = session.pop("username")
    user_id = session.pop("user_id")
    if not username or not user_id:
        return jsonify(error=4006, errmsg='用户未登录')
    try:
        user = User.query.filter(User.nick_name == username).first()
    except Exception as e:
        current_app.log.error(e)
        return jsonify(error=4006, errmsg='未查到用户，退出失败')
    return jsonify('退出账户成功', 204)


@user_blueprint.route('/register', methods=['post'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    phone_num = request.form.get('phone_num')
    print(f'username -> {username}')
    if password != password2:
        return jsonify(errmsg='两次密码不一致')
    try:
        User.nick_name = username
        User.password = password
        User.phone_num = phone_num
        db.session.commit()
    except Exception as e:
        current_app.log.error(e)
        return jsonify(error=5001, errmsg='注册失败，请重试')
    # return redirect(url_for('login'))
    return jsonify('注册成功', 201)


@user_blueprint.errorhandler(404)
def not_found_page(e):
    return '别看了，啥也找不到！！！'

