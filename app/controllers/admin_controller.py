from app.models.tables import Usagers, Articles, Commentaires, Balises, ArticleBalise
from flask import render_template, request, redirect, url_for, flash
from app.ext.database import db
from flask_login import login_required, current_user
from datetime import datetime


@login_required
def index():
    return render_template('index.html')

# ------------------------------------------------------
#               Controllers Usagers
# ------------------------------------------------------

@login_required
def usagers():
    usagers = Usagers.query.all()
    return render_template('liste_usagers.html', usagers=usagers)

@login_required
def createUsager():
    return render_template('create_usager.html')

@login_required
def  storeUsager():
    username = request.values.get('username')
    email = request.values.get('email')
    password = request.values.get('password')
    profil_id = 0
    new_usager = Usagers(username=username, email=email, password=password, profil_id=profil_id)
    db.session.add(new_usager)
    db.session.commit()
    flash('Utilisateur enregistré!')
    return redirect(url_for('admin.usagers'))

@login_required
def showUsager(usager_id):
    usager = Usagers.query.get(usager_id)
    commentaires = Commentaires.query.all()
    print(usager)
    return render_template('show_usager.html', usager = usager, commentaires=commentaires)

@login_required
def updateUsager(usager_id):
    usager = Usagers.query.get_or_404(usager_id)
    if request.method == 'POST':
        usager.username = request.form['username']
        usager.email = request.form['email']
        usager.profil_id = int(request.form['profil_id'])
        db.session.commit()
        flash("L'utilisateur " + usager.username + " a été mis à jour")
        return redirect(url_for('admin.usagers'))

    return render_template('update_usager.html', usager = usager)

@login_required
def destroyUsager(usager_id):
    commentaires = Commentaires.query.all()
    for commentaire in commentaires:
        if commentaire.usager_id == usager_id:
            destroyCommentaireUsager(commentaire.id)
    usager = Usagers.query.get_or_404(usager_id)
    db.session.delete(usager)
    db.session.commit()
    flash('L\'usager a été supprimé!')
    return redirect(url_for('admin.usagers'))

@login_required
def destroyCommentaireUsager(commentaire_id):
    commentaire = Commentaires.query.get_or_404(commentaire_id)
    db.session.delete(commentaire)
    db.session.commit()
    flash('Le commentaire a été supprimé')
    return redirect(url_for('admin.showUsager', usager_id=commentaire.usager_id))

# ------------------------------------------------------
#               Controllers Articles
# ------------------------------------------------------

@login_required
def articles():
    articles = Articles.query.filter(Articles.statut == 1)
    return render_template('liste_articles.html', articles=articles)

@login_required
def createArticle():
    balises = Balises.query.all()
    return render_template('create_article.html', balises=balises)

@login_required
def storeArticle():
    title=request.values.get('title')
    text=request.values.get('text')
    new_article = Articles(title=title, text=text, usager_id=current_user.id, statut=0)
    db.session.add(new_article)
    balise_id = request.values.get('balise_id')
    if balise_id is not None:
        balise_id = int(balise_id)
    balise = request.values.get('balise')
    if balise is not None and balise != "":
        balise_id = storeBalise(balise)
    article = Articles.query.filter(Articles.title==title).first()
    new_article_balise = ArticleBalise(article_id=article.id, balise_id=balise_id)
    db.session.add(new_article_balise)
    db.session.commit()
    flash('Article enregistré!')
    if current_user.profil_id == 1:
        return redirect(url_for('admin.articles'))
    else:
        return redirect(url_for('auteur.articles'))

@login_required
def showArticle(article_id):
    article = Articles.query.get(article_id)
    commentaires = Commentaires.query.all()
    print(article)
    return render_template('show_article.html', article=article, commentaires=commentaires)

@login_required
def updateArticle(article_id):
    article = Articles.query.get_or_404(article_id)
    balises = Balises.query.all()
    if request.method == 'POST':
        article.title = request.form['title']
        article.text = request.form['text']
        balise_id = request.values.get('balise_id')
        if balise_id is not None:
            balise_id = int(balise_id)
        balise = request.values.get('balise')
        if balise is not None and balise != "":
            balise_id = storeBalise(balise)
        old_article_balise = ArticleBalise.query.filter(ArticleBalise.article_id==article.id).first()
        db.session.delete(old_article_balise)
        new_article_balise = ArticleBalise(article_id=article.id, balise_id=balise_id)
        db.session.add(new_article_balise)
        db.session.commit()
        flash("L'article " + article.title + " a été mis à jour")
        if current_user.profil_id == 1:
            return redirect(url_for('admin.articles'))
        else:
            return redirect(url_for('auteur.articles'))

    return render_template('update_article.html', article=article, balises=balises)

@login_required
def publishArticle(article_id):
    article = Articles.query.get_or_404(article_id)
    article.statut=1
    db.session.commit()
    flash("L'article " + article.title + " a été publié")
    if current_user.profil_id == 1:
        return redirect(url_for('admin.articles'))
    else:
        return redirect(url_for('auteur.articles'))


@login_required
def destroyArticle(article_id):
    commentaires = Commentaires.query.all()
    for commentaire in commentaires :
        if commentaire.article_id == article_id :
            destroyCommentaireArticle(commentaire.id)
    article = Articles.query.get_or_404(article_id)
    article_balise = ArticleBalise.query.filter(ArticleBalise.article_id == article_id).first()
    db.session.delete(article_balise)
    db.session.delete(article)
    db.session.commit()
    flash('L\'article a été supprimmé')
    if current_user.profil_id == 1 :
        return redirect(url_for('admin.articles'))
    else :
        return redirect(url_for('auteur.articles'))

@login_required
def destroyCommentaireArticle(commentaire_id):
    commentaire = Commentaires.query.get_or_404(commentaire_id)
    db.session.delete(commentaire)
    db.session.commit()
    flash('Le commentaire a été supprimmé')
    return redirect(url_for('admin.showArticle', article_id=commentaire.article_id))

# ------------------------------------------------------
#               Controllers Balises
# ------------------------------------------------------

@login_required
def storeBalise(balise) -> int :
    new_balise = Balises(description=balise)
    db.session.add(new_balise)
    db.session.commit()
    flash('Catégorie enregistrée !')
    return new_balise.id