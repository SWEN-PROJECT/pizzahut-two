import os
from flask_wtf import form
from app import app, login_manager
from flask import render_template, url_for, redirect, flash, request, session, send_from_directory
from flask_login import logout_user, current_user, login_required
from .forms import LoginForm, SignupForm, ItemForm
from AppController import LSHandler, MenuHandler
from app.models import Euser
from werkzeug.utils import secure_filename
from DBManager import UserManager
from Users import User

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
                return redirect(url_for('dashboard'))
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
@app.route("/menu")
@login_required
def menu():
    if not current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        iform = ItemForm()
        ctrl = MenuHandler.MenuHandler()
        if request.method == 'POST':
            if iform.validate_on_submit():
                #saves the file to the uploads folder 
                image = form.image.data
                imagename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))

                attempt = ctrl.MenuHandler(iform.name.data, iform.price.data, iform.tag.data, iform.description.data, imagename)
                results = ctrl.addItem()
                flash('Item Successfully Added Saved', 'success')
                return redirect(url_for('menu'))
            flash_errors(form)
        else:
            items = ctrl.viewHandle()
    return render_template('menu.html', items=items, type=current_user.u_type, edit_form = iform)


"""Edit Profile Method"""
@login_required
@app.route("/edit-profile")
def editProfile():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else: 
        updateForm = SignupForm()
        handler = LSHandler.LSHandler()
        cUser = handler.loadCustomer()
        
        if request.method == 'POST':
            if updateForm.validate_on_submit():
                updatedCustomer = handler.signupHandle(sform.username.data,sform.password.data,sform.fname.data,sform.lname.data, sform.streetname.data,sform.streetnum.data,sform.town.data,sform.parish.data,sform.telenum.data,  sform.email.data)
            pass

        else:
            if cUser == "N":
                flash('N', 'danger')
        return render_template('editprofile.html',form=updateForm, user=cUser)
            # 
            #     pass
            # 
            #     
            #         
            #         #return redirect(url_for('editProfile'))
            #         return render_template('editprofile.html',form=updateForm)
            #     else:
            #         pass
        # except:
        #     pass
            #flash('Unable to load user information', 'danger')
            #return redirect(url_for('editProfile'))
#             print(cUser.uname)
#             """
#             manager = UserManager.UserManager()
#             temp = User.User(session["uname"])
#             result = manager.queryUser(temp)

#             result = db.session.query(Euser).filter_by(u_name=user.getUname()).all()
#             if result == []:
#                 return None
#             result = result[0]
#             print(result)
#             #return result
#         #except:
#             #return None
#

"""Retrieve Item Route"""
@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']),filename)

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