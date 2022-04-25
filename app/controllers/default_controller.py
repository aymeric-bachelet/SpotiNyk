import flask
from app.models.tables import Usagers, Articles, Commentaires, Balises, ArticleBalise, Reactions, ArticleReaction
from app.models.forms import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.ext.database import db


#Controller HomePage
def index():
    articles = Articles.query.all()
    article_lc = {}
    for article in articles:
        likes = db.session.query(ArticleReaction).filter(ArticleReaction.reaction_id == 1, ArticleReaction.article_id == article.id).count()
        claps = db.session.query(ArticleReaction).filter(ArticleReaction.reaction_id == 2, ArticleReaction.article_id == article.id).count()

        article_lc[article.id] = {}
        article_lc[article.id]['likes'] = likes
        article_lc[article.id]['claps'] = claps

    balises = Balises.query.all()
    commentaires = Commentaires.query.all()
    article_balise = ArticleBalise.query.all()
    balise = request.values.get('balise')
    if balise is None or balise =="":
        balise_id = None
    else :
        balise_id = int(balise)
    return render_template('index.html', articles=articles, commentaires=commentaires, article_balise=article_balise, balises=balises, balise_id=balise_id)

# ------------------------------------------------------
#               Controllers Connexion
# ------------------------------------------------------

def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        passwd = form.password.data
        usager = Usagers.query.filter_by(username=username).first()
        next = flask.request.args.get("next")
        if usager and check_password_hash(usager.password, passwd):
            login_user(usager)
            flash('Connexion réussie')
            #print("next: " + next)
        else:
            flash('Connexion invalide')
            print("Connexion invalide")
        return flask.redirect(next or flask.url_for('default.index'))
    return render_template("login.html", form = form)

def logout():
    logout_user()
    return redirect('/')

def signin():
    return render_template('signin.html')

def storeLecteur():
    username = request.values.get('username')
    email = request.values.get('email')
    password = request.values.get('password')
    profil_id = 0
    new_usager = Usagers(username=username, email=email, password=password, profil_id=profil_id)
    db.session.add(new_usager)
    db.session.commit()
    flash('Utilisateur enregistré!')
    return redirect(url_for('default.login'))

# ------------------------------------------------------
#               Controllers Comments
# ------------------------------------------------------

@login_required
def storeCommentaire():
    article_id = int(request.values.get('article_id'))
    description = request.values.get('description')
    usager_id = current_user.id
    new_commentaire = Commentaires(article_id=article_id, description=description, usager_id=usager_id)
    db.session.add(new_commentaire)
    db.session.commit()
    flash('Commentaire enregistré!')
    return redirect(url_for('default.index'))

# ------------------------------------------------------
#               Controllers Reactions
# ------------------------------------------------------

@login_required
def storeReaction():
    article_id = int(request.values.get('article_id'))
    usager_id = current_user.id
    reaction_id = int(request.values.get('reaction_id'))
    old_article_reaction = ArticleReaction.query.filter(ArticleReaction.article_id==article_id, ArticleReaction.usager_id==usager_id).first()
    article_reaction = ArticleReaction(article_id=article_id, usager_id=usager_id, reaction_id=reaction_id)
    if old_article_reaction is not None :
        db.session.delete(old_article_reaction)
    db.session.add(article_reaction)
    db.session.commit()
    flash('Commentaire enregistré!')
    return redirect(url_for('default.index'))