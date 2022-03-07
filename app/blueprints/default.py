from flask import Blueprint
from app.controllers import default_controller, user_controller

# Blueprint Default:

bp_default = Blueprint('default',__name__, url_prefix="/")

bp_default.route("/")(default_controller.index)
bp_default.route("/login", methods=['GET', 'POST'])(default_controller.login)
bp_default.route("/logout")(default_controller.logout)


# Blueprint Users:

bp_users = Blueprint('users', __name__,url_prefix="/users")

bp_users.route('/',methods=['GET'])(user_controller.index)
bp_users.route('/create', methods=['GET'])(user_controller.create)
bp_users.route('/store', methods=['POST'])(user_controller.store)
bp_users.route('/<int:user_id>', methods=['GET'])(user_controller.show)
bp_users.route('/<int:user_id>/edit', methods=['GET','POST'])(user_controller.update)
bp_users.route('/<int:user_id>', methods=['DELETE'])(user_controller.destroy)