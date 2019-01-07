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
    return jsonify(error=200, errmsg='登录成功')


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
    try:
        user.last_login = time.time()
        db.session.commit()
    except Exception as e:
        current_app.log.error(e)
        return jsonify(error=4006, errmsg='更新用户最后登录时间失败')
    return redirect(url_for('index'))


@user_blueprint.route('/register', methods=['post'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if password != password2:
        return jsonify(errmsg='两次密码不一致')
    try:
        User.nick_name = username
        User.password = password
        db.session.commit()
    except Exception as e:
        current_app.log.error(e)
        return jsonify(error=5001, errmsg='注册失败，请重试')
    return redirect(url_for('login'))


@user_blueprint.errorhandler(404)
def not_found_page(e):
    return '别看了，啥也找不到！！！'

