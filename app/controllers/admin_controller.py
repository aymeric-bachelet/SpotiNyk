from app.models.tables import User, Post
from flask import render_template, request, redirect, url_for, flash
from app.ext.database import db
from flask_login import login_required

@login_required
def index():
    return render_template('admin_home.html')

@login_required
def users():
    users = User.query.all()
    return render_template('list_users.html', users=users)

@login_required
def create():
    return render_template('create_user.html')

@login_required
def  store():
    username = request.values.get('username')
    email = request.values.get('email')
    password = request.values.get('password')
    admin = False
    new_user = User(username=username, email=email, password=password, admin=admin)
    db.session.add(new_user)
    db.session.commit()
    flash('Utilisateur enregistré!')
    return redirect(url_for('admin.index'))

@login_required
def show(user_id):
    user = User.query.get(user_id)
    print(user)
    return render_template('show_user.html', user = user)

@login_required
def update(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash("L'utilisateur " + user.username + " a été mis à jour") 
        return redirect(url_for('admin.index'))

    return render_template('update_user.html', user = user) 

@login_required
def destroy(user_id):
    def destroy(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted!')
        return redirect(url_for('admin.index'))

@login_required
def posts():
    posts = Post.query.all()
    return render_template('list_posts.html', posts=posts)

@login_required
def createPost():
    return render_template('create_post.html')

@login_required
def  storePost():

    return redirect(url_for('admin.index'))

@login_required
def showPost(post_id):
    post = Post.query.get(post_id)
    print(post)
    return render_template('show_post.html', post=post)

@login_required
def updatePost(post_id):
    post = Post.query.get_or_404(post_id)


    return render_template('update_post.html', post=post)

@login_required
def destroyPost(post_id):
    def destroy(post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post has been deleted!')
        return redirect(url_for('admin.index'))