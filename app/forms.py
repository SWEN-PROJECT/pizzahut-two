from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, TextField, FloatField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed 
from datetime import date

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
    username = StringField("Username", validators = [DataRequired()])
    npassword = PasswordField("New Password", validators=[EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Repeat Password")
    streetname = StringField("Street Name", validators=[InputRequired()])
    streetnum = IntegerField("Street Number", validators=[InputRequired()])
    town = StringField("Town", validators=[InputRequired()])
    parish = StringField("Parish", validators=[InputRequired()])
    telenum = IntegerField("Telephone Number", validators=[InputRequired()])
    email = TextField('Email', validators=[InputRequired()])

class ItemForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    price= FloatField("Price", validators = [DataRequired()])
    tag = SelectField("Tag", choices=[('Pizza', 'Pizza'), ('Beverage', 'Beverage'),('Side', 'Side'), ('Crust','Crust'), ('Topping','Topping') ])
    description = TextAreaField("Descripton", validators = [DataRequired()])
    image= FileField("Image", validators=[FileRequired(), FileAllowed(['jpg','png'])])

class StaffForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])

class ReportForm(FlaskForm):
    reptype = SelectField("Report Type", choices=[('Sales', 'Sales'), ('Cancelled', 'Cancelled')])
    year = SelectField("Year", choices=[ (str(i), str(i)) for i in range(int(date.today().strftime('%Y'))-5, int(date.today().strftime('%Y'))+1)])
    month = SelectField("Month", choices=[(str(i),str(i)) for i in range(1,13)]) 
    day = SelectField("Day", choices=[(str(i),str(i)) for i in range(1,32)])
    filter_by = SelectField('Filter', choices=[('Day', 'Day'), ('Month', 'Month'), ('Year', 'Year')], validators = [DataRequired()])