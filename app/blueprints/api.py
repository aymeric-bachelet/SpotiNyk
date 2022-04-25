from flask import Blueprint
from app.controllers import api_controller

# Blueprint Api:

bp_api = Blueprint('api',__name__, url_prefix="/api")

bp_api.route("/", methods=['GET'])(api_controller.index)

bp_api.route("/usagers", methods=['GET'])(api_controller.listeUsagers)
bp_api.route('/usagers/<int:usager_id>', methods=['GET'])(api_controller.showUsager)
bp_api.route('/usagers/', methods=['PUT'])(api_controller.createUsager)
bp_api.route('/usagers/', methods=['POST'])(api_controller.updateUsager)
bp_api.route('/usagers/<int:usager_id>', methods=['DELETE'])(api_controller.destroyUsager)


bp_api.route("/articles", methods=['GET'])(api_controller.listeArticles)
bp_api.route('/articles/<int:article_id>', methods=['GET'])(api_controller.showArticle)
bp_api.route('/articles/', methods=['PUT'])(api_controller.createArticle)
bp_api.route('/articles/', methods=['POST'])(api_controller.updateArticle)
bp_api.route('/articles/<int:article_id>', methods=['DELETE'])(api_controller.destroyArticle)