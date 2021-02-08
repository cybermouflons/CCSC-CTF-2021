import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from webapp.config import config_mapping
from webapp.lcg import PRNG

# instantiate the extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()


def create_app():

    env = os.getenv(
        "FLASK_ENV", "development"
    )
    os.environ["FLASK_ENV"] = env
    config_obj = config_mapping[env]
    
    # instantiate the app
    app = Flask(
        __name__,
        template_folder="./templates",
        static_folder="./static",
    )

    # set config
    app.config.from_object(config_obj)

    # set prng
    app.prng = PRNG()

    # set up extensions
    login_manager.init_app(app)
    bcrypt.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from webapp.user.views import user_blueprint
    from webapp.main.views import main_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(main_blueprint)

    # flask login
    from webapp.models import User

    login_manager.login_view = "user.login"
    login_manager.login_message_category = "danger"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    # error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
