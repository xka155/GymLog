from os import urandom
from flask import Flask
from .routes.index import index
from .api import register

def create_app(name=""):
    if not name:
        name = __name__

    app = Flask(name)
    app.secret_key = urandom(50)
    
    app.register_blueprint(index)

    register.register_api(app)
    
    return app

