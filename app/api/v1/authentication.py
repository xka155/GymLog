from flask import Blueprint
from . import URL_PREFIX

auth = Blueprint('auth', __name__, url_prefix=URL_PREFIX)

@auth.route('/login')
def show():
    return "hello"