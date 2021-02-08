import datetime

from flask import current_app

from webapp.server import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode("utf-8")
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<User {0}>".format(self.email)


class ChessGame(db.Model):

    __tablename__ = "games"

    id = db.Column(db.String(), primary_key=True)
    rated = db.Column(db.String(), nullable=False)
    turns = db.Column(db.Integer, nullable=False)
    victory_status = db.Column(db.String(), nullable=False)
    winner = db.Column(db.String(), nullable=False)
    opening_name = db.Column(db.String(), nullable=False)
    moves = db.Column(db.String(), nullable=False)

    def __init__(self, id, rated, turns, victory_status, winner, opening_name, moves):
        self.id = id
        self.rated = rated
        self.turns = turns
        self.victory_status = victory_status
        self.winner = winner
        self.opening_name = opening_name
        self.moves= moves
   
    def get_id(self):
        return self.id

    def __repr__(self):
        return "<ChessGame {0}>".format(self.id)