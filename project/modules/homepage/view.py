from flask import render_template, request, jsonify, current_app

from . import homepage_blueprint


@homepage_blueprint.route("", methods=["GET"])
def homepage():
    return render_template("homepage/homepage_base_index.html", methods=["GET"])


@homepage_blueprint.route("/history", methods=["GET"])
def history():
    return render_template("homepage/historic.html", methods=["GET"])


@homepage_blueprint.route("/beautiful", methods=["GET"])
def beautiful():
    return render_template("homepage/beautiful.html", methods=["GET"])


@homepage_blueprint.route("/tourism", methods=["GET"])
def tourism():
    return render_template("homepage/tourism.html", methods=["GET"])


@homepage_blueprint.route("/delicacy", methods=["GET"])
def delicacy():
    return render_template("homepage/delicacy.html", methods=["GET"])


@homepage_blueprint.route("/new", methods=["GET"])
def new():
    return render_template("homepage/new.html", methods=["GET"])


@homepage_blueprint.route("/leave", methods=["GET"])
def leave():
    return render_template("homepage/leave.html", methods=["GET"])


@homepage_blueprint.route("/connection", methods=["GET"])
def connection():
    return render_template("homepage/connection.html", methods=["GET"])


@homepage_blueprint.route("/about", methods=["GET"])
def about():
    return render_template("homepage/about.html", methods=["GET"])
