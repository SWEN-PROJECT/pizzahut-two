import os
from flask_wtf import form
from app import app, login_manager
from flask import render_template, url_for, redirect, flash, request, session, send_from_directory, jsonify
from flask_login import logout_user, current_user, login_required
from .forms import LoginForm, SignupForm, ItemForm, UpdateUserForm, StaffForm, ReportForm
from AppController import LSHandler, MenuHandler, ReportHandler
from app.models import Euser
from werkzeug.utils import secure_filename
from .globals import order_handler, menu_handler

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
                if current_user.u_type == 'S':
                    return redirect(url_for('dashboard'))
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
    session['logged-in'] = True   #lol at all
    if (current_user.u_type == "C"): #dis deven funny 
        ctrl = LSHandler.LSHandler()
        rp = ctrl.getRewards(current_user.uid)
        return render_template('dashboard.html', type=current_user.u_type, points=rp)
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

                if "addform" in request.form:
                    attempt = ctrl.addHandle(name, price, tag, description, imagename)
                    if (attempt == "S"): 
                        flash('Item Successfully Added Saved', 'success')
                        return redirect(url_for('menu'))
                    elif (attempt == "F"): 
                        flash('Item Not Added', 'danger') 
                        return redirect(url_for('menu'))
                    else: 
                        flash('Item name is taken.', 'danger')
                        return redirect(url_for('menu'))
                else:
                    itemid = request.form.get("itemid")
                    attempt = ctrl.editHandle(itemid, name, price, tag, description, imagename)
                    if (attempt == "S"): 
                        flash('Item Successfully Edited', 'success')
                        return redirect(url_for('menu'))
                    elif (attempt == "F"): 
                        flash('Item Not Edited', 'danger') 
                        return redirect(url_for('menu'))
                    else: 
                        flash('Item Does Not Exist', 'danger')
                        return redirect(url_for('menu'))
            else:  flash_errors(form)
    if (current_user.u_type == "C"):
        ctrl = LSHandler.LSHandler()
        rp = ctrl.getRewards(current_user.uid)
        return render_template('menu.html', items=items, type=current_user.u_type, edit_form = form, points=rp)
    return render_template('menu.html', items=items, type=current_user.u_type, edit_form = form)

@app.route('/menu/<int:itemID>', methods=['GET'])
def retrieve(itemID):
    global menu_handler
    result = menu_handler.retrieveHandle(itemID)
    return result

"""Update Current Order"""
@app.route('/menu/<int:itemID>', methods=['POST'])
@login_required
def updateCO(itemID):
    global order_handler
    result = order_handler.addToOrder(itemID)
    return f"{result}"

@app.route('/menu/<int:itemID>', methods=['DELETE'])
@login_required
def deleteitem(itemID):
    global menu_handler
    result = menu_handler.deleteHandle(itemID)
    return f'{result}'
    
   

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
        result = order_handler.confirm(request.form.get('type'), request.form.get('points'))
        return f'{result}'
    return "Order Not Confirmed"

"""Displaying all menu items"""
@login_required
@app.route("/vieworders")
def vieworders():
    global order_handler
    result = order_handler.assembleAll()
    if result == []: return render_template('staff.html', orders=result, orderdict=result)
    else: return render_template('staff.html', orders=result[0], orderdict=result[1])

""" Marking an order as complete"""
@login_required
@app.route("/markcomplete <int:order_num>")
def markcomplete(order_num):
    global order_handler
    result = order_handler.markComplete(order_num)
    return redirect(url_for('vieworders'))

""" Marking an order as cancelled """
@login_required
@app.route("/markcancelled <int:order_num>")
def markcancelled(order_num):
    global order_handler
    result = order_handler.markCancelled(order_num)
    return redirect(url_for('vieworders'))

""" Reroutes to checked out page after successful order """
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

"""Add a staff account"""
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

""" Generate a report """
@login_required
@app.route('/report', methods=['POST', 'GET'])
def generate_rep():
    rform = ReportForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            ctrl = ReportHandler.ReportHandler()
            filter_by = str(request.form.get("filter_by")) 
            if filter_by == "Day":
                reptype = request.form.get("reptype")
                if str(reptype) == "Sales":
                    rep = "Complete"
                else:
                    rep = "Cancelled"
                itemsdict, price = ctrl.dayReport(request.form.get("day"), request.form.get("month"), request.form.get("year"), rep)
                return render_template('reports.html',form = rform, items=itemsdict, total=price, reptype = reptype)
            elif filter_by == "Month":
                reptype = request.form.get("reptype")
                if str(reptype) == "Sales":
                    rep = "Complete"
                else:
                    rep = "Cancelled"
                itemsdict, price = ctrl.monthReport(request.form.get("month"), request.form.get("year"), rep)
                return render_template('reports.html',form = rform, items=itemsdict, total=price, reptype = reptype)
            elif filter_by == "Year":
                reptype = request.form.get("reptype")
                if str(reptype) == "Sales":
                    rep = "Complete"
                else:
                    rep = "Cancelled"
                itemsdict, price = ctrl.yearReport(request.form.get("year"), rep)
                return render_template('reports.html',form = rform, items=itemsdict, total=price, reptype = reptype)
    return render_template('reports.html', form = rform, items=None, total=None, reptype = None)

"""Yannik Lyn Fatt"""

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

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