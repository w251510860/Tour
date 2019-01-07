from flask import Blueprint
from . import view

user_blueprint = Blueprint('user', __name__, url_prefix='user')
