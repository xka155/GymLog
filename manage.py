from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.app import create_app
from app.config import app_config

app = create_app()

# Get DB
db = app_config.app['db']

migrate = Migrate(app, db, directory='app/migrations')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def list_routes():
    "List Flask routes"
    
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    
    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    manager.run()