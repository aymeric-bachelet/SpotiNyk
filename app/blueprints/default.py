from flask import Blueprint
from app.controllers import default_controller, admin_controller

# Blueprint Default:

bp_default = Blueprint('default',__name__, url_prefix="/")

bp_default.route("/", methods=['GET'])(default_controller.index)
bp_default.route("/login", methods=['GET', 'POST'])(default_controller.login)
bp_default.route("/logout")(default_controller.logout)
bp_default.route('/comment/store', methods=['POST'])(default_controller.storeComment)


# Blueprint Admins:

bp_admin = Blueprint('admin', __name__, url_prefix="/admin")

bp_admin.route('/', methods=['GET'])(admin_controller.index)
bp_admin.route('/users', methods=['GET'])(admin_controller.users)
bp_admin.route('/users/create', methods=['GET'])(admin_controller.create)
bp_admin.route('/users/store', methods=['POST'])(admin_controller.store)
bp_admin.route('/users/show/<int:user_id>', methods=['GET'])(admin_controller.show)
bp_admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])(admin_controller.update)
bp_admin.route('/users/delete/<int:user_id>', methods=['GET'])(admin_controller.destroy)

bp_admin.route('/posts', methods=['GET'])(admin_controller.posts)
bp_admin.route('/posts/create', methods=['GET'])(admin_controller.createPost)
bp_admin.route('/posts/store', methods=['POST'])(admin_controller.storePost)
bp_admin.route('/posts/show/<int:post_id>', methods=['GET'])(admin_controller.showPost)
bp_admin.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])(admin_controller.updatePost)
bp_admin.route('/posts/delete/<int:post_id>', methods=['GET'])(admin_controller.destroyPost)

bp_admin.route('/category/store', methods=['POST'])(admin_controller.storeCategory)