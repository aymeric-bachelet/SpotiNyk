from app.models.tables import User, Post, Category
from flask import render_template, request, redirect, url_for, flash
from app.ext.database import db
from flask_login import login_required

@login_required
def index():
    return render_template('index.html')

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
    return redirect(url_for('admin.users'))

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
        return redirect(url_for('admin.users'))

    return render_template('update_user.html', user = user) 

@login_required
def destroy(user_id):
    def destroy(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted!')
        return redirect(url_for('admin.users'))

@login_required
def posts():
    posts = Post.query.all()
    return render_template('list_posts.html', posts=posts)

@login_required
def createPost():
    categorys = Category.query.all()
    return render_template('create_post.html', categorys=categorys)

@login_required
def storePost():
    title=request.values.get('title')
    body=request.values.get('body')
    pub_date=request.values.get('pub_date')
    category_id=int(request.values.get('category_id'))
    new_post = Post(title=title, body=body, pub_date=pub_date, category_id=category_id)
    db.session.add(new_post)
    db.session.commit()
    flash('Article enregistré!')
    return redirect(url_for('admin.posts'))

@login_required
def showPost(post_id):
    post = Post.query.get(post_id)
    print(post)
    return render_template('show_post.html', post=post)

@login_required
def updatePost(post_id):
    post = Post.query.get_or_404(post_id)
    categorys = Category.query.all()
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        db.session.commit()
        flash("L'article " + post.title + " a été mis à jour")
        return redirect(url_for('admin.posts'))

    return render_template('update_post.html', post=post, categorys=categorys)

@login_required
def destroyPost(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!')
    return redirect(url_for('admin.posts'))