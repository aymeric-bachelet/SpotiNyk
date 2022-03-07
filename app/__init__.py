from flask import Flask
from app.blueprints.default import bp_default, bp_users
from app.ext import database, migration
from app.ext import appearance
from app.ext import login

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    appearance.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    
    login.init_app(app)

    app.register_blueprint(bp_default)
    app.register_blueprint(bp_users)

    return app