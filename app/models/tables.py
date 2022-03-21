from app.ext.database import db
from datetime import datetime
from werkzeug.security import generate_password_hash

# ------------------------------------------------------
#                      Model ArticleBalise
# ------------------------------------------------------

class ArticleBalise(db.Model):
    __tablename__ = 'Article-balise'

    id = db.Column(db.Integer, primary_key=True)

    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    balise_id = db.Column(db.Integer, db.ForeignKey('balises.id'), nullable=False)

    article = db.relationship("Articles", back_populates="article_balise")
    balise = db.relationship("Balises", back_populates="article_balise")

    def __repr__(self):
        return str(repr(self.balise))

# ------------------------------------------------------
#                      Model ArticleReaction
# ------------------------------------------------------

class ArticleReaction(db.Model):
    __tablename__ = 'Article-reaction'

    id = db.Column(db.Integer, primary_key=True)
    
    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    reaction_id = db.Column(db.Integer, db.ForeignKey('reactions.id'), nullable=False)
    usager_id = db.Column(db.Integer, db.ForeignKey('usagers.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint(article_id, reaction_id, usager_id),)

    article = db.relationship("Articles", back_populates="article_reaction")
    reaction = db.relationship("Reactions", back_populates="article_reaction")
    usager = db.relationship("Usagers")

    def __repr__(self):
        return str(repr(self.usager) + " " + repr(self.reaction) + " " + repr(self.article))

# ------------------------------------------------------
#                      Model Usagers
# ------------------------------------------------------
class Usagers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profil_id = db.Column(db.Integer, db.ForeignKey('profils.id'), nullable=False)

    def __init__(self, username, email, password, profil_id, **kwargs):
        super(Usagers, self).__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.profil_id = profil_id

    def __repr__(self):
        return '%r' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

# ------------------------------------------------------
#                      Model Profils
# ------------------------------------------------------

class Profils(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Profil %r>' % self.description

# ------------------------------------------------------
#                      Model Articles
# ------------------------------------------------------

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_revision = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usager_id = db.Column(db.Integer, db.ForeignKey('usagers.id'), nullable=False)
    statut = db.Column(db.Integer, nullable=False)

    usager = db.relationship('Usagers', backref=db.backref('articles', lazy=True))
    article_balise = db.relationship("ArticleBalise", back_populates="article")
    article_reaction = db.relationship("ArticleReaction", back_populates="article")

    def __repr__(self):
        return '<Article %r>' % self.title


# ------------------------------------------------------
#                      Model Balises
# ------------------------------------------------------

class Balises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)

    article_balise = db.relationship("ArticleBalise", back_populates="balise")

    def __repr__(self):
        return '%r' % self.description

# ------------------------------------------------------
#                      Model Commentaires
# ------------------------------------------------------

class Commentaires(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    usager_id = db.Column(db.Integer, db.ForeignKey('usagers.id'), nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    usager = db.relationship('Usagers', backref=db.backref('commentaires', lazy=True))
    article = db.relationship('Articles', backref=db.backref('commentaires', lazy=True))

    def __repr__(self):
        return '<Commentaire %r>' % self.commentaire

# ------------------------------------------------------
#                      Model Reactions
# ------------------------------------------------------

class Reactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)

    article_reaction = db.relationship("ArticleReaction", back_populates="reaction")

    def __repr__(self):
        return '<Reaction %r>' % self.commentaire