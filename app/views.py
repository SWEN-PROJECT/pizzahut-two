from flask_wtf import form
from app import app
from flask import render_template, url_for, redirect, flash, request, session
from .forms import LoginForm, SignupForm
from pizzahut import UserManager, Customer, User


@app.route("/")
def landing():
    session.pop('logged-in', None)
    return render_template('landing.html')

"""Log in method which logs already registered users into the system."""
@app.route("/login", methods=['POST', 'GET'])
def login():
    session.pop('logged-in', None)
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():
            manager = UserManager.UserManager()
            temp = User.User(request.form['username'])
            result = manager.queryUser(temp)
            if result == None:
                flash('This Username or/and Password does not correspond to a User', 'danger')
            elif manager.decrypt_password(result.getPassword(), request.form['password']):
                return redirect(url_for('dashboard'))
            else:
                flash('Cannot log in', 'danger')
        else:
            flash_errors(lform)
    return render_template('login.html', form = lform)

"""Sign up view method which takes form data, processes it and adds Customer to DB"""
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    session.pop('logged-in', None)
    sform = SignupForm()
    if request.method == 'POST':
        #flash('Post successful', 'success')
        if sform.validate_on_submit():
            #flash('Form validated', 'success')
            #STORE IN DATABASE
            manager = UserManager.UserManager()
            temp = User.User(request.form['username'])
            uservalid = manager.queryUser(temp) 
            if uservalid == None:
                customer = Customer.Customer(sform.username.data,sform.password.data,sform.fname.data,sform.lname.data,
                sform.streetname.data,sform.streetnum.data,sform.town.data,sform.parish.data,sform.telenum.data,
                sform.email.data)
                message = manager.insertUser(customer)         #Stores whether the user was added or not.   
                #flash(message)
                
                if message == "User added":
                    flash('Your account has been created!', 'success')
                    return redirect(url_for('login'))
                elif message == "User Wrong":
                    flash('USER WRONG.', 'danger')
                else:
                    flash('User was not successfully created.', 'danger')
                    return redirect(url_for('signup'))
            else:
                flash('Username is taken.', 'danger')
                return redirect(url_for('signup'))
        else:
            #flash error message
            flash_errors(sform)
    return render_template('signup.html', form = sform)

@app.route("/dashboard")
def dashboard():
    session['logged-in'] = True
    session['type'] = 'M'
    return render_template('dashboard.html', type=session['type'])

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


### Additional Code Created by Yanncick Lynn Fatt
# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)