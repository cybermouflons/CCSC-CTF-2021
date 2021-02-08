import datetime

from flask import current_app

from webapp import db, bcrypt


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


class ParsedGame(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    pgn = db.Column(db.String(), nullable=False)
    is_parsed = db.Column(db.Boolean, nullable=False)
    logs = db.Column(db.String(), nullable=False)
    moves= db.Column(db.String(), nullable=True)
    moves_count = db.Column(db.Integer, nullable=True)
    event = db.Column(db.String(), nullable=True)
    site = db.Column(db.String(), nullable=True)
    white = db.Column(db.String(), nullable=True)
    black = db.Column(db.String(), nullable=True)
    date = db.Column(db.String(), nullable=True) 
    
    def get_id(self):
        return self.id

    def __repr__(self):
        return "<ParsedGame {0}>".format(self.id)