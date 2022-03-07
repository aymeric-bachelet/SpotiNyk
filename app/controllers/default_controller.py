import flask
from app.models.tables import User
from app.models.forms import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash

def index():
    return render_template('index.html')

def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        passwd = form.password.data
        user = User.query.filter_by(username=username).first()
        next = flask.request.args.get("next")
        if user and check_password_hash(user.password, passwd):
            login_user(user)
            flash('Logged in successfully.')
            print("next: " + next)
        else:
            flash('Invalid login.')
            print("invalid login")
        
        return flask.redirect(next or flask.url_for('default.index')) 
        
    return render_template("login.html", form = form)

def logout():
    logout_user()
    return redirect('/')

