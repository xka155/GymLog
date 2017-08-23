from .v1 import authentication

def register_api(app):
    _register_api_v1(app)


def _register_api_v1(app):
    app.register_blueprint(authentication.auth)
