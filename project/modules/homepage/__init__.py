from flask import Blueprint

homepage_blueprint = Blueprint("homepage", __name__, url_prefix="/")
from . import view