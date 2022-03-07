import pytest
from app import create_app
from app.models.tables import User
from app.ext.database import db

## scope:
### function: pour chaque fonction de test, pytest créera une nouvelle application et la supprimera à la fin
### module: créer une seule application à utiliser dans toutes les fonctions de test

@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    return create_app()



@pytest.fixture(scope='module')
def new_user():
    user = User(email='patkennedy79@gmail.com', username='FlaskIsAwesome')
    return user

# @pytest.fixture(scope='module')
# def init_database():
#     app = create_app()
#     client = app.test_client()
#     with app.app_context:
#         user = User(username="foobar", email="foo@bar.com")
#         db.session.add(user)
#         db.session.commit()
#     yield db
#     db.session.close()

