from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, TextField, FloatField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField,FileRequired,FileAllowed 

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

class UpdateUserForm(FlaskForm):
    opassword = PasswordField("Old Password")
    npassword = PasswordField("New Password")
    streetname = StringField("Street Name")
    streetnum = IntegerField("Street Number")
    town = StringField("Town")
    parish = StringField("Parish")
    telenum = IntegerField("Telephone Number")
    email = TextField('Email')

class ItemForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    price= FloatField("Price", validators = [DataRequired()])
    tag = SelectField("Tag", choices=[('Pizza', 'Pizza'), ('Beverage', 'Beverage'),('Side', 'Side'), ('Crust','Crust'), ('Topping','Topping') ])
    description = TextAreaField("Descripton", validators = [DataRequired()])
    image= FileField("Image", validators=[FileRequired(), FileAllowed(['jpg','png'])])

