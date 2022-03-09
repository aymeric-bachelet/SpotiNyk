import flask
from app.models.tables import User, Post, Comment
from app.models.forms import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.ext.database import db

def index():
    posts = Post.query.all()
    comments = Comment.query.all()
    return render_template('index.html', posts=posts,comments=comments)

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
            #print("next: " + next)
        else:
            flash('Invalid login.')
            print("invalid login")
        
        return flask.redirect(next or flask.url_for('default.index')) 
        
    return render_template("login.html", form = form)

def logout():
    logout_user()
    return redirect('/')

@login_required
def storeComment():
    idPost = request.values.get('idPost')
    commentaire = request.values.get('commentaire')
    id_author = current_user.id
    new_comment = Comment(idPost=idPost, commentaire=commentaire, id_author=id_author)
    db.session.add(new_comment)
    db.session.commit()
    flash('Commentaire enregistré!')
    return redirect(url_for('default.index'))