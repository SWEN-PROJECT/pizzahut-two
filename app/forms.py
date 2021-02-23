from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, TextField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])

class SignupForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    fname = StringField("First Name", validators = [DataRequired()])
    lname = StringField("Last Name", validators = [DataRequired()])
    streetname = StringField("Street Name", validators = [DataRequired()])
    streetnum = IntegerField("Street Number", validators = [DataRequired()])
    town = StringField("Town", validators = [DataRequired()])
    parish = StringField("Parish", validators = [DataRequired()])
    telenum = IntegerField("Telephone Number", validators = [DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])