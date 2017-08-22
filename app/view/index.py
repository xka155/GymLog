from flask import Blueprint, render_template

index_view = Blueprint('index_view', __name__)


@index_view.route('/')
def show():
    return render_template("index.html")
  