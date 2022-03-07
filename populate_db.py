# coding=utf-8
from app import create_app
from app.ext.database import db
from app.models.tables import User, Category, Post

app = create_app()
print('Ce script crée des données pour remplir la base de données.')
with app.app_context():
    print('Ajouter des utilisateurs...')
    admin = User(username='admin', email='admin@example.com', password='123123')
    guest = User(username='guest', email='guest@example.com', password='123123')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    print('done!\n')

    print('Ajout de publications et de catégories...')
    c = Category(name='Web Avancée')
    p1 = Post(title='Cours Web Avancée', body='comment créer une application avec flask?', category = c)

    db.session.add(c)
    db.session.add(p1)
    db.session.commit()

    print('done!\n')

    print(User.query.all())
    print(Category.query.all())
    print(Post.query.all())

    print('ok, tout est prêt. Vous pouvez exécuter l\'application maintenant.')

