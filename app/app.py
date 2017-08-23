from os import urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.index import index
from .api import api_register
from .config import db_config, app_config

def create_app(name=""):
    if not name:
        name = __name__

    app = Flask(name)
    app.secret_key = urandom(50)

    # DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
        username=db_config.username,
        password=db_config.password,
        host=db_config.host,
        port=db_config.port,
        database=db_config.database
    )
    # dialect+driver://username:password@host:port/database

    # Suppress depracation warnings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    # ROUTES
    app.register_blueprint(index)
    api_register.register_api(app)
    
    # UPDATE CONFIG
    app_config.app['context'] = app
    app_config.app['db'] = db

    from .model.user import User
    
    return app

