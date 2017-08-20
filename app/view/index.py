from flask import Blueprint

index_view = Blueprint('index_view', __name__)


@index_view.route('/', defaults={'page': 'index'})
def show(page):
    return "Hello World!"
  