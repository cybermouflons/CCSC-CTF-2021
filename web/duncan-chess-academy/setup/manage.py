import os
import pandas as pd


from flask.cli import FlaskGroup

from webapp.server import create_app, db
from webapp.server.models import User, ChessGame

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@cli.command()
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email="ad@min.com", password="admin", admin=True))
    db.session.commit()


@cli.command()
def create_data():
    """Creates sample data."""
    games_df = pd.read_csv(
        os.path.join(os.path.dirname(__file__), "assets", "games.csv")
    )
    games_df.apply(
        lambda game: db.session.add(
            ChessGame(
                game.id,
                game.rated,
                game.turns,
                game.victory_status,
                game.winner,
                game.opening_name,
                game.moves,
            )
        ),
        axis=1,
    )
    db.session.commit()

if __name__ == "__main__":
    cli()
