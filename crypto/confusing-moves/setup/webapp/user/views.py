import os

from flask import (
    render_template,
    Blueprint,
    url_for,
    redirect,
    flash,
    request,
    current_app,
    send_from_directory
)
from flask_login import login_user, logout_user, login_required, current_user

from webapp import bcrypt, db
from webapp.models import User, ParsedGame
from webapp.user.forms import LoginForm, RegisterForm, PGNForm
from webapp.benny import parse_pgn

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash("User with this email already exists!", "danger")
        else:
            user = User(email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)

            flash("Thank you for registering.", "success")
            return redirect(url_for("user.parser"))

    return render_template("user/register.html", form=form)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("user.parser"))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            flash("You are logged in. Welcome!", "success")
            return redirect(url_for("user.parser"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("user/login.html", form=form)
    return render_template("user/login.html", title="Please Login", form=form)


@user_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out. Bye!", "success")
    return redirect(url_for("main.home"))


@user_blueprint.route("/parser", methods=["GET", "POST"])
@login_required
def parser():
    form = PGNForm(request.form)

    if request.method == "POST" and form.validate():
        is_parsed, parsed_games, logs = parse_pgn(
            request.form["pgn"],
            current_app.prng,
            current_app.config["INTERNAL_PYPI_URL"],
            current_app.config["PUBLIC_PYPI_URL"]
        )
            
        if is_parsed and len(parsed_games) > 0:
            game = ParsedGame(
                pgn=request.form["pgn"],
                is_parsed=is_parsed,
                logs=logs,
                moves=" ".join(parsed_games[0].moves),
                moves_count=len(parsed_games[0].moves),
                event=parsed_games[0].event,
                site=parsed_games[0].site,
                white=parsed_games[0].white,
                black=parsed_games[0].black,
                date=parsed_games[0].date
            )
        else:
            game = ParsedGame(
                pgn=request.form["pgn"],
                is_parsed=False,
                logs=logs,
            )

        db.session.add(game)
        db.session.commit()
        
        flash("Game submitted for parsing successfully!", "success")

    all_parsed_games = ParsedGame.query.all()

    return render_template(
        "user/parser.html", form=form, all_parsed_games=all_parsed_games, game_count=len(all_parsed_games)
    )


@user_blueprint.route("/game/delete", methods=["POST"])
@login_required
def game_delete():
    ## NOTE TO MYSELF: There is an IDOR here.. but it doesn't affect the challenge.
    game = ParsedGame.query.get(request.form['gameid'])

    if game is not None:
        db.session.delete(game)
        db.session.commit()

    return redirect(url_for("user.parser")) 

@user_blueprint.route("/generator", methods=["GET"])
@login_required
def generator():
    path = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(path, ".."), "lcg.py")

