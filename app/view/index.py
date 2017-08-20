from flask import Blueprint

index_view = Blueprint('index_view', __name__)


@index_view.route("/")
def show():
    return "Hello World!"
  