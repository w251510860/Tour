from flask import render_template, g, jsonify, current_app, request

from mock_data import mock_introduce, mock_article
from project.modules.models import Knowledge, Introduce
from utils.common import user_login_data
from . import scenic_blu


@scenic_blu.route('')
@scenic_blu.route('/<int:scenic_id>')
@user_login_data
def scenic(scenic_id=None):
    if not scenic_id:
        scenic_id = 1
    try:
        know = Knowledge.query.filter_by(id=scenic_id).first()
        if not know:
            return jsonify(errno="4104", errmsg='文章不存在，或已删除')
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno="4001", errmsg="数据库查询错误")
    data = {
        "user_info": g.user.to_user_dict() if g.user else None,
        "know": know.to_dict() if know else None
    }
    return render_template('homepage/scenic.html', data=data)


@scenic_blu.route('/scenic_list')
def scenic_list():
    # json_data = request.json
    # per_page = json_data.get('per_page')
    # page_num = json_data.get('page_num')
    per_page = 15
    page_num = 1
    if not all([per_page, page_num]):
        per_page = 15
        page_num = 1
    try:
        paginate = Knowledge.query.paginate(page_num, per_page, False)
        # 获取查询出来的数据
        items = paginate.items
        # 获取到总页数
        total_page = paginate.pages
        current_page = paginate.page
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=4004, errmsg="数据查询失败")
    scenic_li = []
    for item in items:
        scenic_li.append(item.to_dict())
    return jsonify(errno=200, errmsg="OK", totalPage=total_page, currentPage=current_page, newsList=scenic_li)


@scenic_blu.route('/introduce', methods=['GET'])
def introduce():
    name = request.args['name']
    if not name:
        return jsonify(errno="4104", errmsg='文章不存在，或已删除')

    try:
        introduce_content = Introduce.query.filter_by(name=name).first()
        if not introduce:
            return jsonify(errno="4104", errmsg='文章不存在，或已删除')
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=4004, errmsg="数据查询失败")
    data = {
        # "user_info": g.user.to_user_dict() if g.user else None,
        "user_info": None,
        "introduce": introduce_content if introduce else None
    }
    return render_template('homepage/attraction.html', data=data)


@scenic_blu.route('/mock_data')
def mock_data():
    try:
        if Introduce.query.filter_by(id=1).first():
            return '已经有数据了...你想炸库吗？？？'
        mock_article()
        mock_introduce()
    except Exception as e:
        return f'错误'
    return '200'
