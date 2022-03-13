from app.ext.database import db
from datetime import datetime
from werkzeug.security import generate_password_hash

# ------------------------------------------------------
#                      Model User
# ------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.BOOLEAN, nullable=False)

    def __init__(self, username, email, password, admin, **kwargs):
        super(User, self).__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.admin = admin

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
#                      Model Post
# ------------------------------------------------------

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title

# ------------------------------------------------------
#                      Model Category
# ------------------------------------------------------

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '%r' % self.name

# ------------------------------------------------------
#                      Model Comment
# ------------------------------------------------------

class Comment(db.Model):
    idComm = db.Column(db.Integer, primary_key=True)
    commentaire = db.Column(db.String(80), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))

    def __repr__(self):
        return '<Comment %r>' % self.commentaire