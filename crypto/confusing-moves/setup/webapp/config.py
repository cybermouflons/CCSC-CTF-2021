# project/server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "Chess Game Parser")
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    INTERNAL_PYPI_URL = os.getenv("INTERNAL_PYPI_URL","http://0.0.0.0:8080")
    PUBLIC_PYPI_URL = os.getenv("PUBLIC_PYPI_URL","http://0.0.0.0:8081")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{0}".format(os.path.join(basedir, "dev.db"))
    )

class ProductionConfig(BaseConfig):
    """Production configuration."""
    FLASK_DEBUG=0
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///{0}".format(os.path.join(basedir, "prod.db")),
    )
    WTF_CSRF_ENABLED = True

config_mapping = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}