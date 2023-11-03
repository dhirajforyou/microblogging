from flask import Flask
from flask_bootstrap import Bootstrap
from .routes import routes


def register_extensions(app):
    bootstrap = Bootstrap()
    bootstrap.init_app(app)


def create_app():
    app = Flask(__name__)
    # app configuration
    app.config["SECRET_KEY"] = "key that should never be revealed..."
    # serve bootstrap from local. Later in production environment, take from cdn.
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    register_extensions(app)
    app.register_blueprint(routes)
    return app

