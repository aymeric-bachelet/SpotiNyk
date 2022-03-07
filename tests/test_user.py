from app.models.tables import User
from app.ext.database import db

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username and email fields are defined correctly
    """
    assert new_user.username == 'patkennedy'
    assert new_user.email == 'patkennedy79@gmail.com'


def test_new_user_2(client):
    response = client.get("/users/1")
    assert b"foobar" in response.data


    