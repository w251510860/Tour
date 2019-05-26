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
        "know": know.to_dict() if know else None,
        "img": []
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
    img = {
        '南湾湖': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558774667&di=3f52437c158d4bb8ba17599bde491ef1&imgtype=jpg&er=1&src=http%3A%2F%2Fbbswater-fd.zol-img.com.cn%2Ft_s1200x5000%2Fg5%2FM00%2F09%2F0E%2FChMkJ1c7_yKID128AAyP54FdwuQAARlWgOgnyMADI__876.jpg',
        '鸡公山': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2778454299,817872236&fm=26&gp=0.jpg',
        '灵山': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558179992167&di=9accc084fb43a35ca6c0c0ad6cdba93e&imgtype=0&src=http%3A%2F%2Fdpic.tiankong.com%2F7k%2F7e%2FQJ8134668844.jpg',
        '郝堂村': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558180014372&di=64ec7bdc11df6bd144f85901e640c567&imgtype=0&src=http%3A%2F%2Fcdn.moji002.com%2Fimages%2Fsimgs%2F2017%2F03%2F12%2F14893106560.35144100.1308_android.jpg',
        '金牛文化园': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558180042329&di=f252d8de1a54678f23ff704d85a7c656&imgtype=0&src=http%3A%2F%2Fimg624.ph.126.net%2FvCfMbZVQuSlOIDgjpUVdpw%3D%3D%2F3012908150712883043.jpg',
        '黄柏山': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3319692382,2482671114&fm=26&gp=0.jpg',
        '邓颖超祖居': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558180099512&di=c23c51acacaccc8d1a31427bfac13cf2&imgtype=0&src=http%3A%2F%2Fwww.xxkly.cn%2Fupload%2F20170312%2Fthumb_201703120929565329.png',
    }
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
        "introduce": introduce_content if introduce else None,
        "img": img[name]
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
