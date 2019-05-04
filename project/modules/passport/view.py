import datetime

from flask import request, jsonify, current_app, session, make_response

from project import db, redis_db
from project.modules.models import User
from utils.captcha.captcha import captcha
from . import passport_blu


@passport_blu.route('/register', methods=['POST'])
def register():
    json_data = request.json
    username = json_data.get('username')
    password = json_data.get('password')
    phone_num = json_data.get('phone_num')
    print(f'接受注册请求-> {username} {password} {phone_num}')
    if not all([username, password, phone_num]):
        return jsonify(errno="4001", errmsg="参数不全")
    try:
        user = User.query.filter_by(phone_num=phone_num).first()
        if user:
            return jsonify(errno="4003", errmsg="用户已存在")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno="4001", errmsg="数据库查询错误")
    user = User()
    user.nick_name = username
    user.phone_num = phone_num
    user.password = password
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno="4001", errmsg="数据保存错误")
    session['user_id'] = user.id
    session['nick_name'] = user.nick_name
    session['phone_num'] = user.phone_num

    return jsonify(errno="0", errmsg="OK")


@passport_blu.route('/login', methods=['POST'])
def login():
    json_data = request.json
    phone_num = json_data.get('phone_num')
    password = json_data.get('password')
    if not all([phone_num, password]):
        return jsonify(errno="4001", errmsg="参数不全")
    try:
        user = User.query.filter_by(phone_num=phone_num).first()
        if not user:
            return jsonify(errno="4104", errmsg="用户不存在")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno="4001", errmsg="数据库查询错误")
    if password != user.password:
        return jsonify(errno='4106', errmsg="密码错误")
    session['user_id'] = user.id
    session['nick_name'] = user.nick_name
    session['phone_num'] = user.phone_num
    user.last_login = datetime.datetime.now()
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
    return jsonify(errno="0", errmsg="OK")


@passport_blu.route('/logout', methods=['POST'])
def logout():
    print(f'退出登陆')
    session.pop('user_id', None)
    session.pop('nick_name', None)
    session.pop('phone_num', None)
    return jsonify(errno="0", errmsg="OK")


@passport_blu.route('/image_code', methods=['POST', 'GET'])
def image_code():
    code_id = request.args.get('code_id')
    print(f'code_id -> {code_id}')
    name, text, image = captcha.generate_captcha()
    try:
        # 保存当前生成的图片验证码内容
        redis_db.setex('ImageCode_' + code_id, 300, text)
    except Exception as e:
        current_app.logger.error(e)
        return make_response(jsonify(errno=4004, errmsg='保存图片验证码失败'))

        # 返回响应内容
    resp = make_response(image)
    # 设置内容类型
    resp.headers['Content-Type'] = 'image/jpg'
    return resp
