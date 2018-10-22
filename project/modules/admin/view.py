from . import admin_blueprint


from flask import render_template


@admin_blueprint.route("/index")
def index():
    pic_list = [
        "../static/picture/admin_index.jpg",
        "../static/picture/admin_index1.jpg",
        "../static/picture/admin_index2.jpg",
        "../static/picture/admin_index3.jpg",
        "../static/picture/admin_index4.jpg",
    ]
    return render_template("admin_index.html", pic_urls=pic_list)
