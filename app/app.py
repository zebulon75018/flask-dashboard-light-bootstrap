# -*- encoding: utf-8 -*-
"""
Flask Boilerplate
Author: AppSeed.us - App Generator 
"""

# all the imports necessary
from flask import json, url_for, redirect, render_template, flash, g, session, jsonify, request, send_from_directory
from werkzeug.exceptions import HTTPException, NotFound, abort

from flask            import Flask
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt
from flask_mail       import Mail



import os

#from app  import app

from flask       import url_for, redirect, render_template, flash, g, session, jsonify, request, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
# from .         import lm, db, bc
"""
from . models    import User
from . common    import COMMON, STATUS
from . assets    import *
from . forms     import LoginForm, RegisterForm

from . import db
"""
import os, shutil, re, cgi
        
# provide login manager with load_user callback
"""
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""

app = Flask(__name__, static_url_path='/static')

# authenticate user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# register user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # define login form here
    form = RegisterForm(request.form)

    msg = None

    # custommize your pate title / description here
    page_title       = 'Register - FlaskPlay Open-Source Boilerplate | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, registration page.'

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        name     = request.form.get('name'    , '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'
        
        else:                    
            pw_hash = bc.generate_password_hash(password)

            user = User(username, pw_hash, name, email)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'     

    # try to match the pages defined in -> /pages/
    return render_template( 'layouts/default.html',
                            title=page_title,
                            content=render_template( 'pages/register.html', form=form, msg=msg) )

# authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # define login form here
    #form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # custommize your page title / description here
    page_title = 'Login - FlaskPlay Open-Source Boilerplate | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, login page.'

    # check if both http method is POST and form is valid on submit
    
    # try to match the pages defined in -> themes/light-bootstrap/pages/
    return render_template( 'pages/login.html')
                           
# Used only for static export
@app.route('/icons.html')
def icons():

    icons =["nc-air-baloon","nc-album-2","nc-alert-circle-i","nc-align-center","nc-align-left-2","nc-ambulance","nc-app","nc-atom","nc-badge","nc-bag-16","nc-bank","nc-basket","nc-bell-55","nc-bold","nc-book-bookmark","nc-bookmark-2","nc-box-2","nc-box","nc-briefcase-24","nc-bulb-63","nc-bullet-list-67","nc-bus-front-12","nc-button-pause","nc-button-play","nc-button-power","nc-calendar-60","nc-camera-compact","nc-caps-small","nc-cart-simple","nc-chart-bar-32","nc-chart-pie-36","nc-chat-33","nc-check-2","nc-circle-10","nc-cloud-download-93","nc-cloud-upload-94","nc-compass-05","nc-controller-modern","nc-credit-card","nc-delivery-fast","nc-diamond","nc-email-85","nc-favourite-28","nc-glasses-2","nc-globe-2","nc-globe","nc-hat-3","nc-headphones","nc-html5","nc-image","nc-istanbul","nc-key-25","nc-laptop","nc-layout-11","nc-lock-circle-open","nc-map-big","nc-minimal-down","nc-minimal-left","nc-minimal-right","nc-minimal-up","nc-mobile","nc-money-coins","nc-note-03","nc-palette","nc-paper","nc-pin-3","nc-planet","nc-refresh-69","nc-ruler-pencil","nc-satisfied","nc-scissors","nc-send","nc-settings-gear-65","nc-settings","nc-share-66","nc-shop","nc-simple-add","nc-simple-delete","nc-simple-remove","nc-single-02","nc-single-copy-04","nc-sound-wave","nc-spaceship","nc-sun-fog-29","nc-support-17","nc-tablet-2","nc-tag-content","nc-tap-01","nc-tie-bow","nc-tile-56","nc-time-alarm","nc-touch-id","nc-trophy","nc-tv-2","nc-umbrella-13","nc-user-run","nc-vector","nc-watch-time","nc-world-2","nc-zoom-split"]
    # custommize your page title / description here
    page_title = 'Icons - Light Bootstrap Open-Source Flask Dashboard  | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, the icons page.'

    # try to match the pages defined in -> pages/
    return render_template( 'pages/icons.html',icons=icons) 

# Used only for static export
@app.route('/notifications.html')
def notifications():

    # custommize your page title / description here
    page_title = 'Notifications - Light Bootstrap Open-Source Flask Dashboard  | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, the notifications page.'

    # try to match the pages defined in -> pages/
    return render_template( 'pages/notifications.html') 

# Used only for static export
@app.route('/user.html')
def user():

    # custommize your page title / description here
    page_title = 'Profile - Light Bootstrap Open-Source Flask Dashboard  | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, the profile page.'

    # try to match the pages defined in -> pages/
    return render_template( 'pages/user.html') 

    # Used only for static export
@app.route('/table.html')
def table():

    # custommize your page title / description here
    page_title = 'Tables - Light Bootstrap Open-Source Flask Dashboard  | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, the tables page.'

    # try to match the pages defined in -> pages/
    return render_template( 'pages/table.html') 

# Used only for static export
@app.route('/typography.html')
def typography():

    # custommize your page title / description here
    page_title = 'Typography - Light Bootstrap Open-Source Flask Dashboard  | AppSeed App Generator'
    page_description = 'Open-Source Flask Boilerplate, the tables page.'

    # try to match the pages defined in -> pages/
    return render_template('pages/typography.html') 

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        # try to match the pages defined in -> themes/light-bootstrap/pages/
        return render_template('pages/'+path) 
    except Exception as e:
        print(e)
        abort(404)

#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'),
#                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.route('/sitemap.xml')
#def sitemap():
#    return send_from_directory(os.path.join(app.root_pa    th, 'static'),
#                               'sitemap.xml')

# ------------------------------------------------------

# error handling
# most common error codes have been added for now
# TO DO:
# they could use some styling so they don't look so ugly

def http_err(err_code):
	
    err_msg = 'Oups !! Some internal error ocurred. Thanks to contact support.'
	
    if 400 == err_code:
        err_msg = "It seems like you are not allowed to access this link."

    elif 404 == err_code:    
        err_msg  = "The URL you were looking for does not seem to exist."
        err_msg += "<br /> Define the new page in /pages"
    
    elif 500 == err_code:    
        err_msg = "Internal error. Contact the manager about this."

    else:
        err_msg = "Forbidden access."

    return err_msg
    
@app.errorhandler(401)
def e401(e):
    return http_err( 401) # "It seems like you are not allowed to access this link."

@app.errorhandler(404)
def e404(e):
    return http_err( 404) # "The URL you were looking for does not seem to exist.<br><br>
	                      # If you have typed the link manually, make sure you've spelled the link right."

@app.errorhandler(500)
def e500(e):
    return http_err( 500) # "Internal error. Contact the manager about this."

@app.errorhandler(403)
def e403(e):
    return http_err( 403 ) # "Forbidden access."

@app.errorhandler(410)
def e410(e):
    return http_err( 410) # "The content you were looking for has been deleted."


if __name__ == "__main__":
	#db.create_all()

	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)