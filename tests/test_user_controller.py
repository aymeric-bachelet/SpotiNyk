def test_index(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert b"Liste d'utilisateurs" in response.data

def test_store(client):
    response = client.post("/users/store", data={'username':'John Doe', 'email':'johndoe@mail.com'})
    assert b"john Doe" in response.data