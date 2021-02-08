import os


from flask.cli import FlaskGroup

from webapp import create_app, db

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

if __name__ == "__main__":
    cli()
