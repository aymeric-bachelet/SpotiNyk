def test_app_is_created(app):
    assert app.name == 'app'

def test_config_is_loaded(config):
    assert config["DEBUG"] is True

def test_request_returns_404(client):
    assert client.get("/url_does_not_exists").status_code == 404

def test_request_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Home Page'