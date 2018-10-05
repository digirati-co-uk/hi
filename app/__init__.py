from flask import Flask
from config import Config


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.ping.routes import BP as PING_BP
    app.register_blueprint(PING_BP, url_prefix="/ping")
    from app.uuid.routes import BP as UUID_BP
    app.register_blueprint(UUID_BP, url_prefix="/uuid")

    return app
