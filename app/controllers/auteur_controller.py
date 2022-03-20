from app.models.tables import Usagers, Articles, Commentaires, Balises
from flask import render_template, request, redirect, url_for, flash
from app.ext.database import db
from flask_login import login_required, current_user

@login_required
def articles():
    articles = Articles.query.filter(Articles.usager_id == current_user.id)
    return render_template('liste_articles.html', articles=articles)