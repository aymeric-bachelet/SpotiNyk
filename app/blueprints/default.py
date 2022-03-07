from flask import Blueprint
from app.controllers import default_controller, admin_controller

# Blueprint Default:

bp_default = Blueprint('default',__name__, url_prefix="/")

bp_default.route("/")(default_controller.index)
bp_default.route("/login", methods=['GET', 'POST'])(default_controller.login)
bp_default.route("/logout")(default_controller.logout)




# Blueprint Admins:

bp_admin = Blueprint('users', __name__, url_prefix="/users")

bp_admin.route('/', methods=['GET'])(admin_controller.index)
bp_admin.route('/create', methods=['GET'])(admin_controller.create)
bp_admin.route('/store', methods=['POST'])(admin_controller.store)
bp_admin.route('/<int:user_id>', methods=['GET'])(admin_controller.show)
bp_admin.route('/<int:user_id>/edit', methods=['GET', 'POST'])(admin_controller.update)
bp_admin.route('/<int:user_id>', methods=['DELETE'])(admin_controller.destroy)

