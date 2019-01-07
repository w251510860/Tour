from flask import Blueprint
from . import view

homepage_blueprint = Blueprint("homepage", __name__, url_prefix="/")