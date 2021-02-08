from werkzeug.utils import redirect

from flask.helpers import url_for
from flask import Blueprint

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET"])
def home():
    return redirect(url_for("user.login"))
