import datetime

import flask
import json
from flask import jsonify, render_template, request
from app.models.tables import Usagers, Articles, Commentaires, Balises, ArticleBalise, Reactions, ArticleReaction
from app.ext.database import db

def index():
    return render_template('indexAPI.html')

def listeUsagers():
    usagers = Usagers.query.all()
    res = {}
    for usager in usagers :
        res[usager.username] = usager.to_json()
    print(res)
    return jsonify({'message':'ok', 'data': res}), 200

def showUsager(usager_id):
    usager = Usagers.query.get(usager_id)
    return jsonify({'message':'ok', 'data': usager.to_json()}), 200

def createUsager():
    record = json.loads(request.data)
    usager = Usagers(
        username=record['username'],
        email=record['email'],
        password=record['password'],
        profil_id=record['profil_id'])
    db.session.add(usager)
    db.session.commit()
    return jsonify({"message":"usager created", "id":usager.id}),201

def updateUsager():
   record = json.loads(request.data)
   id = record['id']
   usager = Usagers.query.get_or_404(id)
   usager.username = record['username']
   usager.email = record['email']
   db.session.commit()
   return jsonify({"message":"usager updated","id":usager.id}),200

def destroyUsager(usager_id):
    usager = Usagers.query.get_or_404(usager_id)
    db.session.delete(usager)
    db.session.commit()
    return jsonify({"message":"usager deleted"}),204

def listeArticles():
    articles = Articles.query.all()
    res = {}
    for article in articles :
        res[article.title] = article.to_json()
    return jsonify({'message':'ok', 'data': res}), 200

def showArticle(article_id):
    article = Articles.query.get(article_id)
    return jsonify({'message':'ok', 'data': article.to_json()}), 200

def createArticle():
    record = json.loads(request.data)
    article = Articles(
        title=record['title'],
        text=record['text'],
        usager_id=record['usager_id'],
        statut=record['statut'])
    db.session.add(article)
    db.session.commit()
    return jsonify({"message":"article created", "id":article.id}),201

def updateArticle():
   record = json.loads(request.data)
   id = record['id']
   article = Articles.query.get_or_404(id)
   article.title = record['title']
   article.text = record['text']
   article.usager_id = record['usager_id']
   article.statut = record['statut']
   db.session.commit()
   return jsonify({"message":"article updated","id":article.id}),200

def destroyArticle(article_id):
    article = Articles.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({"message":"article deleted"}),204