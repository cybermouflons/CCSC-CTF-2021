from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional


class LoginForm(FlaskForm):
    email = StringField("Email Address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email(message=None),
            Length(min=6, max=40),
        ],
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Confirm password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )


class FilterForm(FlaskForm):
    winner = SelectField(
        "Winner",
        validators=[Optional()],
    )
    opening_name = SelectField(
        "Opening Name",
        validators=[Optional()],
    )
    rated = StringField("Rated", [Length(max=10)])
    turns = IntegerField("Turns", [Optional()])
    victory_status = SelectField(
        "Victory Status",
        validators=[Optional()],
    )

