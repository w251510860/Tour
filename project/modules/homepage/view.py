from flask import render_template, request, jsonify, current_app, session, g, redirect, url_for
from utils.common import user_login_data
from utils.news_scripy import request_news
from . import homepage_blueprint


@homepage_blueprint.route("", methods=["GET"])
@user_login_data
def index():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/homepage_base_index.html", data=data)


@homepage_blueprint.route("/history", methods=["GET"])
@user_login_data
def history():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/historic.html", data=data)


@homepage_blueprint.route("/beautiful", methods=["GET"])
@user_login_data
def beautiful():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/beautiful.html", data=data)


@homepage_blueprint.route("/tourism", methods=["GET"])
@user_login_data
def tourism():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/tourism.html", data=data)


@homepage_blueprint.route("/delicacy", methods=["GET"])
@user_login_data
def delicacy():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/delicacy.html", data=data)


@homepage_blueprint.route("/new", methods=["GET"])
@user_login_data
def new():
    news = request_news()
    data = {
        "news": news if news else None,
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/new.html", data=data)


@homepage_blueprint.route("/leave", methods=["GET"])
@user_login_data
def leave():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/leave.html", data=data)


@homepage_blueprint.route("/connection", methods=["GET"])
@user_login_data
def connection():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/connection.html", data=data)


@homepage_blueprint.route("/about", methods=["GET"])
@user_login_data
def about():
    data = {
        "user_info": g.user.to_user_dict() if g.user else None
    }
    return render_template("homepage/about.html", data=data)
