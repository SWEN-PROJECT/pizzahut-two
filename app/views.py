import os
from flask_wtf import form
from app import app, login_manager
from flask import render_template, url_for, redirect, flash, request, session, send_from_directory, jsonify
from flask_login import logout_user, current_user, login_required
from .forms import LoginForm, SignupForm, ItemForm, UpdateUserForm, StaffForm
from AppController import LSHandler, MenuHandler
from app.models import Euser
from werkzeug.utils import secure_filename
from DBManager import UserManager
from Users import User
from .globals import order_handler

@app.route("/")
def landing():
    return render_template('landing.html')

"""Log in method which logs already registered users into the system."""
@app.route("/login", methods=['POST', 'GET'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():
            ctrl = LSHandler.LSHandler()
            attempt = ctrl.loginHandle(request.form['username'],request.form['password'])
            if (attempt == "N"): flash('No user exists with this password and username.', 'danger')
            elif (attempt == "Y"): 
                flash('Login successful!', 'success')
                session["uname"] = request.form['username']
                return redirect(url_for('dashboard'))
            else: flash('Cannot login as user ' + request.form['username'], 'danger')
        else: 
            flash_errors(lform)
    return render_template('login.html', form = lform)

@login_manager.user_loader
def load_user(id):
    return Euser.query.get(int(id))

@app.route("/logout")
@login_required
def logout():
	session.pop('logged-in', None)
	logout_user()
	return redirect(url_for('landing'))

"""Sign up view method which takes form data, processes it and adds Customer to DB"""
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    sform = SignupForm()
    if request.method == 'POST':
        if sform.validate_on_submit():
            ctrl = LSHandler.LSHandler()
            attempt = ctrl.signupHandle(sform.username.data,sform.password.data,sform.fname.data,sform.lname.data, sform.streetname.data,sform.streetnum.data,sform.town.data,sform.parish.data,sform.telenum.data,  sform.email.data)
            if (attempt == "S"): 
                flash('Account Created!', 'success')
                return redirect(url_for('login'))
            elif (attempt == "F"): 
                flash('Account Not Created!', 'danger') 
                return redirect(url_for('signup'))
            else: flash('Username is taken.', 'danger')
        else:
            #flash error message
            flash_errors(sform)
    return render_template('signup.html', form = sform)



@app.route("/dashboard")
@login_required
def dashboard():
	if not current_user.is_authenticated:
		return redirect(url_for('landing'))
	session['logged-in'] = True
	return render_template('dashboard.html', type=current_user.u_type)

"""Get Menu Method"""
@app.route("/menu", methods=['POST', 'GET'])
@login_required
def menu():
    if not current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        form = ItemForm()
        ctrl = MenuHandler.MenuHandler()
        items = ctrl.viewHandle()
        if request.method == 'POST':
            if form.validate_on_submit():
                name = request.form.get("name")
                price = request.form.get("price")
                tag = request.form.get("tag")
                description = request.form.get("description")

                photo = request.files.get("image")
                imagename = secure_filename(photo.filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))

                attempt = ctrl.addHandle(name, price, tag, description, imagename)

                if (attempt == "S"): 
                    flash('Item Successfully Added Saved', 'success')
                    return redirect(url_for('menu'))
                elif (attempt == "F"): 
                    flash('Item Not Added', 'danger') 
                    return redirect(url_for('menu'))
                else: flash('Item name is taken.', 'danger')
                return redirect(url_for('menu'))
            else:  flash_errors(form)
    return render_template('menu.html', items=items, type=current_user.u_type, edit_form = form)

"""Update Current Order"""
@app.route('/menu/<itemID>', methods=['POST', 'GET'])
def updateCO(itemID):
    global order_handler
    result = order_handler.addToOrder(itemID)
    return f"{result}"

@app.route('/menu/<itemID>', methods=['POST', 'GET'])
@login_required
def deleteitem(itemID):
    print("Print This")
    if not current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        print("I am heeere")
        ctrl = MenuHandler.MenuHandler()
        print("I am here")
        items = ctrl.viewHandle()
        form = ItemForm()
        attempt = ctrl.deleteHandle(itemID)
        if (attempt == "S"): 
            flash('Item Successfully Deleted', 'success')
            return redirect(url_for('menu'))
        elif (attempt == "F"): 
            flash('Item Not Deleted', 'danger') 
            return redirect(url_for('menu'))
        else: flash('Item not found.', 'danger')
        return redirect(url_for('menu'))
        print("Mi deh yah")
    return render_template('menu.html', items=items, type=current_user.u_type, edit_form = form)

"""Checkout Current Order"""
@app.route('/menu/checkout', methods=['POST', 'GET'])
def checkoutCO():
    global order_handler
    result = order_handler.checkout()
    return result

"""Current Order Confirmed"""
@app.route('/menu/confirm', methods=['POST', 'GET'])
def confirmCO():
    global order_handler
    if request.method == 'POST':
        result = order_handler.confirm(request.form.get('type'))
        return f'{result}'
    return "Order Not Confirmed"


@app.route('/complete', methods=['POST', 'GET'])
@login_required
def order_complete():
    global order_handler
    result = order_handler.completion()
    if result != None:
        return render_template('ordercomplete.html', order=result[0], items=result[1])
    else: 
        flash('Order not confirmed.', 'danger')
        return render_template('ordercomplete.html', order='NOK', items='NOK')

"""Edit Profile Method"""
@login_required
@app.route("/edit-profile", methods=["GET","POST"])
def editProfile():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else: 
        handler = LSHandler.LSHandler()
        cUser = handler.loadCustomer()
        updateForm = UpdateUserForm()

        if request.method == 'POST':  
            if updateForm.validate_on_submit():
                if request.form['npassword'] == '' or request.form['npassword'] == None:
                    result = handler.updateHandle(request.form['username'],\
                     '', cUser.getName().getFname(), cUser.getName().getLname(), \
                         request.form['streetname'], request.form['streetnum'], request.form['town'], \
                             request.form['parish'], request.form['telenum'],request.form['email'])
                else:
                    result = handler.updateHandle(request.form['username'],\
                     request.form['npassword'], cUser.getName().getFname(), cUser.getName().getLname(), \
                         request.form['streetname'], request.form['streetnum'], request.form['town'], \
                             request.form['parish'], request.form['telenum'],request.form['email'])
                if (result == "S"): 
                    flash('Account Updated!', 'success')
                    return redirect(url_for('dashboard'))
                elif (result == "F"): 
                    flash('Account Not Updated!', 'danger') 
                    return redirect(url_for('dashboard'))
            flash_errors(updateForm)
    return render_template('editprofile.html',form=updateForm, info=cUser)

"""Retrieve Image Route"""
@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']),filename)



#Add Staff Account 
@login_required
@app.route('/addstaff', methods=['POST', 'GET'])
def addStaff():
    sform = StaffForm()
    if request.method == 'POST':
        if sform.validate_on_submit():
            ctrl = LSHandler.LSHandler()
            attempt = ctrl.staffHandle(sform.username.data,sform.password.data)
            if (attempt == "S"): 
                flash('Account Created!', 'success')
                return redirect(url_for('dashboard'))
            elif (attempt == "F"): 
                flash('Account Not Created!', 'danger') 
                return redirect(url_for('dashboard'))
            else: flash('Username is taken.', 'danger')
        else:
            #flash error message
            flash_errors(sform)
    return render_template('addstaff.html', form = sform)

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

"""Yannik Lyn Fatt"""
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)