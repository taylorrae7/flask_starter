import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)


class Config(object):
    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-key-here'

    # Database setup
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Useful directories
    APP_DIR = os.path.dirname(os.path.abspath(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    STATIC_DIR = os.path.join(APP_DIR, 'app.static')


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

    # Database setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/flask_starter'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    ENV = 'test'
    TESTING = True
    DEBUG = False

    # Dummy secret key for running tests
    SECRET_KEY = 'test'

    # Database setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/flask_starter_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # For faster testing
    BCRYPT_LOG_ROUNDS = 2

    # Allows form testing
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    ENV = 'prod'
    debug = False

    # Database setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/flask_starter_prod'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BCRYPT_LOG_ROUNDS = 10

