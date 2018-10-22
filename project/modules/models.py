from project import db
from datetime import datetime


class BaseModel:
    # 基本模型类--创建和更新的时间
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class CmtLike:
    """
    点赞数和评论数
    """
    like_cnt = db.Column(db.Integer, default=0)  # 点赞数

    cmt_cnt = db.Column(db.Integer, default=0)  # 评论数

    clicks = db.Column(db.Integer, default=0)  # 点击数

"""
用户和常识（攻略）的多对多的关系
"""
the_user_know = db.Table(
    "user_know",
    db.Column("user_id", db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column("know_id", db.Integer, db.ForeignKey('know.id'), primary_key=True),
    db.Column("create_time", db.DateTime, default=datetime.now)
)


class User(BaseModel, db.Model):
    """
    用户表
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 昵称

    sex = db.Column(db.Enum("man", "woman"), default="man")  # 性别

    pic_url = db.Column(db.String(256))   # 头像

    password = db.Column(db.String(128), nullable=False)  # 密码

    phone_num = db.Column(db.String(11), unique=True, nullable=False)  # 电话

    user_live = db.Column(db.String(256))  # 用户所在地

    last_login = db.Column(db.DATETIME, default=datetime.now)  # 最后登录时间

    id_style = db.Column(db.Enum("user", "admin"), default="user")  # 身份类型（用户和管理员）

    # 用户发表的常识(攻略)
    user_know = db.relationship("Knowledge", backref="user", lazy="dynamic")

    # 用户发表的评论
    user_comment = db.relationship("Comment", backref="user", lazy="dynamic")

    # 用户发表的问题
    user_question = db.relationship("Question", backref="user", lazy='dynamic')

    def to_admin_dict(self):
        """
        转化为字典的形式(管理员返回的数据)
        :return:
        """
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
            "pic_url": self.pic_url,
            "phone_num": self.phone_num,
            "last_login": self.last_login
        }

        return resp_dict

    def to_user_dict(self):
        """
        用户返回的数据字典
        :return:
        """
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
            "sex": self.sex,
            "pic_url": self.pic_url,
            "phone_num": self.phone_num,
            "user_live": self.user_live,
            "last_login": self.last_login
        }
        return resp_dict


class Knowledge(BaseModel, CmtLike, db.Model):
    """
    常识（攻略）表
    """

    __tablename__ = "know"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 外键(用户)

    title = db.Column(db.String(128), nullable=False)  # 标题

    content = db.Column(db.Text, nullable=False)  # 内容

    tour_route = db.Column(db.String(256))  # 旅游路线

    advice_time = db.Column(db.String(128))  # 建议时间

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "user": User.query.get(self.user_id).to_user_dict(),
            "content": self.content,
            "title": self.title,
            "tour_route": self.tour_route,
            "advice_time": self.advice_time,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return resp_dict


class Travel(BaseModel, CmtLike, db.Model):
    """
    景点表
    """
    __tablename__ = "travel"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), unique=True, nullable=False)  # 景点名称

    pic_link = db.Column(db.String(256))  # 景点图片

    open_time = db.Column(db.String(128))  # 营业时间

    advice_time = db.Column(db.String(128))  # 建议游玩时间

    phone = db.Column(db.String(11), nullable=False)  # 联系电话

    price = db.Column(db.String(11))   # 门票价格

    website = db.Column(db.String(128))  # 景点网站

    place = db.Column(db.String(256))   # 景点具体地点

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "name": self.name,
            "pic_link": self.pic_link,
            "open_time": self.open_time,
            "advice_time": self.advice_time,
            "phone": self.phone,
            "price": self.price,
            "website": self.website,
            "place": self.place
        }
        return resp_dict


class Comment(BaseModel, CmtLike, db.Model):
    """
    评论表
    """
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   # 外键（用户）

    title = db.Column(db.String(256), nullable=False)   # 评论的标题

    content = db.Column(db.Text, nullable=False)   # 评论内容

    like_degree = db.Column(db.Enum("0", "1", "2", '3', '4', '5'), default="5")  # 评论该景点的喜欢程度（1不喜欢-5最喜欢）

    parent_id = db.Column(db.Integer, db.ForeignKey("comment.id"))   # 父评论的ID

    parent = db.relationship("Comment", remote_side=[id])  # 自关联

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "user": User.query.get(self.user_id).to_user_dict(),
            "title": self.title,
            "content": self.content,
            "like_degree": self.like_degree,
            "parent": self.parent.to_dict() if self.parent else None,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return resp_dict


class Question(BaseModel, db.Model):
    """
    问题表
    """
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))   # 外键（用户）

    content = db.Column(db.String(256), nullable=False)   # 问题内容

    dot_time = db.Column(db.DateTime, default=datetime.now, nullable=False)  # 发布问题的时间点

    cmt_cnt = db.Column(db.Integer, default=0)   # 评论数

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "user": User.query.get(self.user_id).to_user_dict(),
            "content": self.content,
            "dot_time": self.dot_time.strftime("%Y-%m-%d %H:%M:%S"),
            "cmt_cnt": self.cmt_cnt,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return resp_dict


