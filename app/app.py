from flask import Flask
from .view.index import index_view

APP = Flask(__name__)


def create_app(name=""):
    if not name:
        name = __name__

    app = Flask(name)
    app.register_blueprint(index_view)

    return app

