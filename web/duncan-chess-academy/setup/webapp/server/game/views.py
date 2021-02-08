from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_required

from webapp.server import db
from webapp.server.models import ChessGame
from webapp.server.game.forms import AddGameForm


game_blueprint = Blueprint("game", __name__)

# Comment out in production ... only need this in dev...
# @game_blueprint.route("/add", methods=["GET", "POST"])
# @login_required
def add():
    form = AddGameForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            game = ChessGame(
                id=form.id.data,
                rated=form.rated.data,
                turns=form.turns.data,
                victory_status=form.victory_status.data,
                winner=form.winner.data,
                opening_name=form.on.data,
                moves=form.moves.data
            )
            db.session.add(game)
            db.session.commit()

            flash("Game Added Successfully!", "success")
            return redirect(url_for("user.members"))
        else:

            for fieldName, errorMessages in form.errors.items():
                for err in errorMessages: 
                    print(fieldName, err)
    
    return render_template("game/add.html", form=form)