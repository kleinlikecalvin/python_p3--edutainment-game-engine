from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# import sqlalchemy as sa
# from app import db


class create_deck(FlaskForm):
    deck_title = StringField(("Username"), validators=[DataRequired()])
    deck_subject = PasswordField(("Password"), validators=[DataRequired()])
    deck_color = BooleanField(("Remember Me"))
    submit = SubmitField(("Sign In"))
