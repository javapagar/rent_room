import os

from flask_api.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])