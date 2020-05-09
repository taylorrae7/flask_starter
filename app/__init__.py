import logging
import os

from flask import Flask, render_template, request as req
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    """ Factory for creating app """

    app = Flask(__name__, instance_relative_config=True)

    config_obj = os.getenv("APP_SETTINGS", default="config.DevelopmentConfig")
    app.config.from_object(config_obj)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    app.logger.setLevel(logging.NOTSET)
    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app


def register_extensions(app):
    """ Configures flask extensions """

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Bcrypt
    bcrypt.init_app(app)

    # Setup Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


def register_blueprints(app):
    """ Registers blueprint """

    from app.views import home_bp, auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)


def register_errorhandlers(app):
    """ Register custom error pages """

    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{}.html'.format(error_code)), error_code

    for errcode in [401, 403, 404, 410]:
        app.errorhandler(errcode)(render_error)

