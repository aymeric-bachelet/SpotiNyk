from flask_login.login_manager import LoginManager

from app.models.tables import Usagers

lm = LoginManager()

def init_app(app):
    lm.init_app(app)
    lm.login_view = 'default.login' #définir login_view : indiquer à Flask l'URL d'authentification des utilisateurs

    @lm.user_loader
    def load_usager(usager_id):
        return Usagers.query.get(usager_id)
    