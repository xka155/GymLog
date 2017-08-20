import os
from app.app import create_app


MODE = os.environ['MODE']

app = create_app()

if MODE != "dev":
    app.run()
