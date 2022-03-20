from flask import Blueprint
from app.controllers import default_controller, admin_controller, auteur_controller

# Blueprint Default:

bp_default = Blueprint('default',__name__, url_prefix="/")

bp_default.route("/", methods=['GET'])(default_controller.index)
bp_default.route("/login", methods=['GET', 'POST'])(default_controller.login)
bp_default.route("/logout")(default_controller.logout)
bp_default.route("/signin", methods=['GET'])(default_controller.signin)
bp_default.route("/lecteur/store", methods=['POST'])(default_controller.storeLecteur)
bp_default.route('/commentaire/store', methods=['POST'])(default_controller.storeCommentaire)
bp_default.route('/reaction/store', methods=['POST'])(default_controller.storeReaction)


# Blueprint Admins:

bp_admin = Blueprint('admin', __name__, url_prefix="/admin")

    #usagers
bp_admin.route('/', methods=['GET'])(admin_controller.index)
bp_admin.route('/usagers', methods=['GET'])(admin_controller.usagers)
bp_admin.route('/usagers/create', methods=['GET'])(admin_controller.createUsager)
bp_admin.route('/usagers/store', methods=['POST'])(admin_controller.storeUsager)
bp_admin.route('/usagers/show/<int:usager_id>', methods=['GET'])(admin_controller.showUsager)
bp_admin.route('/usagers/<int:usager_id>/edit', methods=['GET', 'POST'])(admin_controller.updateUsager)
bp_admin.route('/usagers/delete/<int:usager_id>', methods=['GET'])(admin_controller.destroyUsager)
bp_admin.route('/comments/delete/<int:commentaire_id>', methods=['GET'])(admin_controller.destroyCommentaireUsager)

    #posts
bp_admin.route('/articles', methods=['GET'])(admin_controller.articles)
bp_admin.route('/articles/create', methods=['GET'])(admin_controller.createArticle)
bp_admin.route('/articles/store', methods=['POST'])(admin_controller.storeArticle)
bp_admin.route('/articles/show/<int:article_id>', methods=['GET'])(admin_controller.showArticle)
bp_admin.route('/articles/<int:article_id>/edit', methods=['GET', 'POST'])(admin_controller.updateArticle)
bp_admin.route('/articles/<int:article_id>/publish', methods=['GET', 'POST'])(admin_controller.publishArticle)
bp_admin.route('/articles/delete/<int:article_id>', methods=['GET'])(admin_controller.destroyArticle)
bp_admin.route('/comments/delete/<int:commentaire_id>', methods=['GET'])(admin_controller.destroyCommentaireArticle)

    #balises
bp_admin.route('/balise/store', methods=['POST'])(admin_controller.storeBalise)


# Blueprint Auteur:
bp_auteur = Blueprint('auteur', __name__, url_prefix="/auteur")

bp_auteur.route('/articles', methods=['GET'])(auteur_controller.articles)