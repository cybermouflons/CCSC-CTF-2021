from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class AddGameForm(FlaskForm):
    id = StringField(
        "ID",
        validators=[DataRequired(), Length(min=6, max=40),],
    )
    rated = StringField(
        "Rated", validators=[DataRequired(), Length(max=10)]
    )
    turns = IntegerField(
        "Turns", validators=[DataRequired()]
    )
    victory_status = StringField(
        "Victory Status", validators=[DataRequired()]
    )
    winner = StringField(
        "Winner", validators=[DataRequired()]
    )
    on = StringField(
        "Opening Name", validators=[DataRequired()]
    )
    moves = StringField(
        "Moves", validators=[DataRequired()]
    )