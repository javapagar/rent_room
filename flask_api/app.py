from flask import Flask
from flask_api.rest import room, health


def create_app(config_name):
    app = Flask(__name__)

    config_module = f"flask_api.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(room.blueprint)
    app.register_blueprint(health.blueprint)

    return app
