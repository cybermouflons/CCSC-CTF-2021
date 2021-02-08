import pandas as pd

from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from webapp.server import bcrypt, db
from webapp.server.models import User
from webapp.server.user.forms import LoginForm, RegisterForm, FilterForm
from webapp.server.models import ChessGame
from webapp.server.game.views import add

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
            return redirect(url_for("user.members"))

    return render_template("user/register.html", form=form)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("user.members"))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
            user.password, request.form["password"]
        ):
            login_user(user)
            flash("You are logged in. Welcome!", "success")
            return redirect(url_for("user.members"))
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


@user_blueprint.route("/members", methods=["GET", "POST"])
@login_required
def members():
    games_df = pd.DataFrame(
        [
            {
                "id": g.id,
                "opening_name": g.opening_name,
                "winner": g.winner,
                "moves": g.moves,
                "victory_status": g.victory_status,
                "rated": g.rated,
                "turns": g.turns,
            }
            for g in ChessGame.query.all()
        ]
    )

    form = FilterForm(request.form)
    form.opening_name.choices = [""] + list(games_df["opening_name"].unique())
    form.victory_status.choices = [""] + list(games_df["victory_status"].unique())
    form.winner.choices = [""] + list(games_df["winner"].unique())

    if request.method == "POST":
        if form.validate():
            searchable_fields = [
                "winner",
                "opening_name",
                "victory_status",
                "rated",
                "turns",
            ]

            for field, value in request.form.items():
                if value and field in searchable_fields:
                    games_df = games_df.query(f"{field} == '{value}'")

        else:
            flash("Error submitting filter form", "danger")

    return render_template(
        "user/members.html", form=form, games=games_df.to_dict(orient="records")
    )
